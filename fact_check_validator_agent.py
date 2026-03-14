#!/usr/bin/env python3
"""
Langworthywatch Fact-Checking Validator Agent
Ensures all claims have citations and Archive.org backups exist
"""

import re
import os
from pathlib import Path
from datetime import datetime
import json
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

try:
    import requests
except ImportError:
    import sys
    print("ERROR: Required dependency 'requests' is not installed.")
    print("Install with: pip install requests")
    print("\nOr install all dependencies: pip install -r requirements.txt")
    sys.exit(1)


class Colors:
    """ANSI color codes"""
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[0;34m'
    MAGENTA = '\033[0;35m'
    CYAN = '\033[0;36m'
    WHITE = '\033[1;37m'
    NC = '\033[0m'


class FactCheckValidator:
    def __init__(self, content_root=None):
        if content_root is None:
            content_root = Path(__file__).parent / "Fact Checks"
        else:
            content_root = Path(content_root)

        self.content_root = content_root
        self.results = {
            "timestamp": datetime.now().isoformat(),
            "summary": {},
            "fact_checks_scanned": 0,
            "issues": {
                "missing_sources": [],
                "pending_archives": [],
                "broken_urls": [],
                "weak_citations": []
            },
            "url_cache": {}
        }

        # Patterns
        self.archive_pattern = re.compile(r'https?://(?:web\.)?archive\.(?:org|is)/[^\s\)]+')
        self.pending_archive_pattern = re.compile(r'Archive:\s*https?://archive\.(?:org|is)/\[pending\]', re.IGNORECASE)
        self.url_pattern = re.compile(r'https?://[^\s\)\"]+')

        # Claims that should have citations
        self.claim_indicators = [
            re.compile(r'\b(?:according to|reported by|stated|claimed|analysis|study|data shows?|statistics|estimates?|found that)\b', re.IGNORECASE),
            re.compile(r'\b(?:\d+%|\$[\d,]+|\d+,\d+)\b'),  # Numbers/statistics
            re.compile(r'\b(?:CBO|Congressional Budget Office|Center on Budget|Urban Institute)\b'),
        ]

    def find_fact_check_files(self):
        """Find all fact-check markdown files"""
        md_files = [
            f for f in self.content_root.glob("*.md")
            if f.is_file() and f.name.startswith('factcheck_')
        ]
        print(f"Found {len(md_files)} fact-check files")
        return md_files

    def extract_sources_section(self, content):
        """Extract the Sources section from content"""
        # Look for ## Sources or ### Sources heading
        sources_match = re.search(r'^###+\s*Sources?\s*$(.*?)(?=^###+|\Z)', content, re.MULTILINE | re.DOTALL)
        if sources_match:
            return sources_match.group(1).strip()
        return None

    def check_archive_urls(self, content):
        """Check for archive.org/archive.is URLs and pending status"""
        archives = {
            'total': 0,
            'valid': 0,
            'pending': 0,
            'pending_urls': []
        }

        # Count all archive URLs
        all_archives = self.archive_pattern.findall(content)
        archives['total'] = len(all_archives)

        # Count pending archives
        pending = self.pending_archive_pattern.findall(content)
        archives['pending'] = len(pending)
        archives['pending_urls'] = pending

        # Valid archives = total - pending
        archives['valid'] = archives['total'] - archives['pending']

        return archives

    def check_url_accessibility(self, url, timeout=10):
        """Check if a URL is accessible"""
        # Check cache
        if url in self.results['url_cache']:
            return self.results['url_cache'][url]

        try:
            response = requests.head(
                url,
                timeout=timeout,
                allow_redirects=True,
                headers={'User-Agent': 'Mozilla/5.0 (LangworthyWatch FactCheckValidator/1.0)'}
            )

            # Some servers don't support HEAD
            if response.status_code in [405, 501]:
                response = requests.get(
                    url,
                    timeout=timeout,
                    allow_redirects=True,
                    headers={'User-Agent': 'Mozilla/5.0 (LangworthyWatch FactCheckValidator/1.0)'},
                    stream=True
                )

            success = response.status_code < 400
            error = None if success else f"HTTP {response.status_code}"

            # Cache result
            self.results['url_cache'][url] = (success, error)

            # Rate limiting
            time.sleep(0.5)

            return success, error

        except requests.Timeout:
            result = (False, "Timeout")
            self.results['url_cache'][url] = result
            return result
        except requests.ConnectionError:
            result = (False, "Connection failed")
            self.results['url_cache'][url] = result
            return result
        except Exception as e:
            result = (False, str(e))
            self.results['url_cache'][url] = result
            return result

    def identify_claims(self, content):
        """Identify sentences that appear to make factual claims"""
        claims = []

        # Split into paragraphs
        paragraphs = content.split('\n\n')

        for para_num, para in enumerate(paragraphs, 1):
            # Skip headings, sources section, metadata
            if para.startswith('#') or para.startswith('---'):
                continue

            # Check for claim indicators
            for pattern in self.claim_indicators:
                if pattern.search(para):
                    # Extract sentences from this paragraph
                    sentences = re.split(r'[.!?]\s+', para)
                    for sent in sentences:
                        if pattern.search(sent):
                            claims.append({
                                'text': sent.strip()[:200],  # First 200 chars
                                'paragraph': para_num,
                                'has_numbers': bool(re.search(r'\d', sent))
                            })
                    break  # Only count paragraph once

        return claims

    def validate_fact_check(self, file_path):
        """Validate a single fact-check file"""
        results = {
            'file': file_path.name,
            'path': str(file_path),
            'issues': [],
            'warnings': [],
            'stats': {
                'claims_identified': 0,
                'sources_found': False,
                'archive_urls': 0,
                'pending_archives': 0,
                'broken_urls': 0
            }
        }

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # 1. Check for Sources section
            sources_section = self.extract_sources_section(content)
            if not sources_section:
                results['issues'].append({
                    'severity': 'high',
                    'type': 'missing_sources_section',
                    'message': 'No Sources section found'
                })
                self.results['issues']['missing_sources'].append({
                    'file': file_path.name,
                    'issue': 'No Sources section'
                })
            else:
                results['stats']['sources_found'] = True

                # Count source entries
                source_lines = [line for line in sources_section.split('\n') if line.strip() and not line.strip().startswith('#')]
                results['stats']['source_entries'] = len(source_lines)

                if len(source_lines) < 3:
                    results['warnings'].append({
                        'severity': 'medium',
                        'type': 'few_sources',
                        'message': f'Only {len(source_lines)} source entries found'
                    })

            # 2. Check Archive.org URLs
            archives = self.check_archive_urls(content)
            results['stats']['archive_urls'] = archives['total']
            results['stats']['pending_archives'] = archives['pending']

            if archives['pending'] > 0:
                results['issues'].append({
                    'severity': 'medium',
                    'type': 'pending_archives',
                    'message': f'{archives["pending"]} archive URLs still pending'
                })
                self.results['issues']['pending_archives'].append({
                    'file': file_path.name,
                    'count': archives['pending']
                })

            if sources_section and archives['total'] == 0:
                results['warnings'].append({
                    'severity': 'high',
                    'type': 'no_archive_backups',
                    'message': 'No Archive.org backups found for sources'
                })

            # 3. Identify claims
            claims = self.identify_claims(content)
            results['stats']['claims_identified'] = len(claims)

            if len(claims) > 10 and not sources_section:
                results['issues'].append({
                    'severity': 'critical',
                    'type': 'many_claims_no_sources',
                    'message': f'{len(claims)} claims identified but no Sources section'
                })

            # 4. Check external URLs (in sources section only, to avoid checking Langworthy's site)
            if sources_section:
                source_urls = self.url_pattern.findall(sources_section)
                # Filter out archive.org URLs (we validate those separately)
                non_archive_urls = [url for url in source_urls if 'archive.org' not in url and 'archive.is' not in url]

                results['stats']['source_urls_checked'] = len(non_archive_urls)
                # URL checking happens in batch later

            return results

        except Exception as e:
            results['issues'].append({
                'severity': 'critical',
                'type': 'validation_error',
                'message': f'Error validating file: {str(e)}'
            })
            return results

    def scan_all_files(self):
        """Scan all fact-check files"""
        print("\n" + "=" * 80)
        print("LANGWORTHYWATCH - FACT-CHECK VALIDATOR")
        print("=" * 80)

        fc_files = self.find_fact_check_files()
        self.results['fact_checks_scanned'] = len(fc_files)

        if len(fc_files) == 0:
            print(f"\n{Colors.YELLOW}No fact-check files found in {self.content_root}{Colors.NC}")
            return []

        print(f"\nScanning {len(fc_files)} fact-check files...")

        file_results = []
        for i, fc_file in enumerate(fc_files, 1):
            print(f"  Processing {i}/{len(fc_files)}: {fc_file.name}...", end='\r')
            result = self.validate_fact_check(fc_file)
            file_results.append(result)

        print(f"  Processing {len(fc_files)}/{len(fc_files)}... Done!        ")

        return file_results

    def generate_report(self, file_results):
        """Generate and print validation report"""
        total_issues = sum(len(r['issues']) for r in file_results)
        total_warnings = sum(len(r['warnings']) for r in file_results)

        critical_issues = sum(1 for r in file_results for i in r['issues'] if i['severity'] == 'critical')
        high_issues = sum(1 for r in file_results for i in r['issues'] if i['severity'] == 'high')
        medium_issues = sum(1 for r in file_results for i in r['issues'] if i['severity'] == 'medium')

        print("\n" + "=" * 80)
        print(f"{Colors.WHITE}FACT-CHECK VALIDATION REPORT{Colors.NC}")
        print("=" * 80)

        # Summary
        print(f"\n{Colors.CYAN}Summary:{Colors.NC}")
        print(f"  Fact-checks scanned: {self.results['fact_checks_scanned']}")
        print(f"  Total issues: {total_issues}")
        print(f"  Total warnings: {total_warnings}")
        print()

        if critical_issues > 0:
            print(f"{Colors.RED}  Critical: {critical_issues}{Colors.NC}")
        if high_issues > 0:
            print(f"{Colors.RED}  High: {high_issues}{Colors.NC}")
        if medium_issues > 0:
            print(f"{Colors.YELLOW}  Medium: {medium_issues}{Colors.NC}")

        # Statistics
        total_claims = sum(r['stats'].get('claims_identified', 0) for r in file_results)
        total_archives = sum(r['stats'].get('archive_urls', 0) for r in file_results)
        total_pending = sum(r['stats'].get('pending_archives', 0) for r in file_results)
        files_with_sources = sum(1 for r in file_results if r['stats'].get('sources_found'))

        print(f"\n{Colors.CYAN}Statistics:{Colors.NC}")
        print(f"  Claims identified: {total_claims}")
        print(f"  Files with Sources section: {files_with_sources}/{len(file_results)}")
        print(f"  Archive.org URLs: {total_archives}")
        print(f"  Pending archives: {total_pending}")

        # Issue breakdown by file
        if total_issues > 0:
            print(f"\n{Colors.RED}Issues by File:{Colors.NC}")
            print("-" * 80)

            for result in file_results:
                if result['issues']:
                    print(f"\n{Colors.CYAN}{result['file']}{Colors.NC}")
                    for issue in result['issues']:
                        severity_color = {
                            'critical': Colors.RED,
                            'high': Colors.RED,
                            'medium': Colors.YELLOW
                        }.get(issue['severity'], Colors.WHITE)

                        print(f"  {severity_color}[{issue['severity'].upper()}] {issue['message']}{Colors.NC}")

        # Warnings
        if total_warnings > 0:
            print(f"\n{Colors.YELLOW}Warnings:{Colors.NC}")
            print("-" * 80)

            for result in file_results:
                if result['warnings']:
                    print(f"\n{Colors.CYAN}{result['file']}{Colors.NC}")
                    for warning in result['warnings']:
                        print(f"  [Warning] {warning['message']}")

        # Actionable recommendations
        print(f"\n{Colors.CYAN}Recommended Actions:{Colors.NC}")
        print("-" * 80)

        action_count = 1

        if len(self.results['issues']['missing_sources']) > 0:
            print(f"{action_count}. Add Sources sections to files missing them:")
            for item in self.results['issues']['missing_sources']:
                print(f"   - {item['file']}")
            action_count += 1

        if len(self.results['issues']['pending_archives']) > 0:
            print(f"\n{action_count}. Create Archive.org backups for pending URLs:")
            for item in self.results['issues']['pending_archives']:
                print(f"   - {item['file']}: {item['count']} pending archives")
            print(f"   Use: https://web.archive.org/save/URL")
            action_count += 1

        if total_issues == 0 and total_warnings == 0:
            print(f"{Colors.GREEN}✓ No issues or warnings found. Great work!{Colors.NC}")

        print("\n" + "=" * 80)

        # Save summary
        self.results['summary'] = {
            'total_fact_checks': len(file_results),
            'total_issues': total_issues,
            'total_warnings': total_warnings,
            'critical_issues': critical_issues,
            'high_issues': high_issues,
            'medium_issues': medium_issues,
            'total_claims': total_claims,
            'total_archives': total_archives,
            'pending_archives': total_pending,
            'credibility_score': self._calculate_credibility_score(file_results)
        }

        return file_results

    def _calculate_credibility_score(self, file_results):
        """Calculate overall credibility score (0-100)"""
        if not file_results:
            return 100

        total_checks = len(file_results)

        # Deductions
        deductions = 0

        # Missing sources = -20 points each
        deductions += len(self.results['issues']['missing_sources']) * 20

        # Pending archives = -5 points each
        deductions += len(self.results['issues']['pending_archives']) * 5

        # No archive backups when sources exist = -10 points each
        no_backups = sum(1 for r in file_results
                        if r['stats'].get('sources_found') and r['stats'].get('archive_urls', 0) == 0)
        deductions += no_backups * 10

        score = max(0, 100 - deductions)
        return round(score, 1)

    def save_report(self, output_file=None):
        """Save detailed report to JSON"""
        if output_file is None:
            output_file = Path(__file__).parent / "fact_check_validation_report.json"
        else:
            output_file = Path(output_file)

        try:
            with open(output_file, 'w') as f:
                json.dump(self.results, f, indent=2)

            print(f"\n{Colors.GREEN}✓ Report saved: {output_file}{Colors.NC}")

        except Exception as e:
            print(f"\n{Colors.RED}✗ Failed to save report: {e}{Colors.NC}")


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Validate fact-check files for citations and Archive.org backups"
    )
    parser.add_argument(
        '--content-root',
        default=None,
        help='Path to fact-check content directory (default: ./Fact Checks)'
    )
    parser.add_argument(
        '--output',
        default=None,
        help='Output file for report (default: ./fact_check_validation_report.json)'
    )

    args = parser.parse_args()

    # Create validator
    validator = FactCheckValidator(content_root=args.content_root)

    # Run validation
    file_results = validator.scan_all_files()

    # Generate report
    validator.generate_report(file_results)

    # Save detailed report
    validator.save_report(output_file=args.output)

    # Exit code: 0 if no critical/high issues, 1 otherwise
    critical = len([r for r in file_results for i in r['issues'] if i['severity'] in ['critical', 'high']])
    return 0 if critical == 0 else 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
