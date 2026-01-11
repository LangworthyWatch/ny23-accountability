#!/usr/bin/env python3
"""
Langworthywatch Scraper Monitoring Agent
Monitors scraper health, logs metrics, and alerts on failures
"""

import subprocess
import json
import sys
from datetime import datetime
from pathlib import Path
import re


class ScraperMonitor:
    def __init__(self, project_dir=None):
        if project_dir is None:
            project_dir = Path(__file__).parent
        else:
            project_dir = Path(project_dir)

        self.project_dir = project_dir
        self.log_file = project_dir / "monitor_log.jsonl"
        self.summary_file = project_dir / "monitor_summary.json"
        self.results = {
            "timestamp": datetime.now().isoformat(),
            "date": datetime.now().strftime("%Y-%m-%d"),
            "time": datetime.now().strftime("%H:%M:%S"),
            "status": "unknown",
            "scrapers": {},
            "metrics": {},
            "errors": [],
            "warnings": []
        }

    def run_scraper(self, timeout=300):
        """Run the scraper and capture output"""
        print("=" * 80)
        print("SCRAPER MONITOR - Starting scraper run...")
        print("=" * 80)

        try:
            # Run scraper with timeout
            result = subprocess.run(
                [sys.executable, 'run_scraper.py'],
                cwd=self.project_dir,
                capture_output=True,
                text=True,
                timeout=timeout
            )

            # Parse output
            output = result.stdout
            errors = result.stderr

            # Store raw output for debugging
            self.results["raw_output"] = output
            self.results["raw_errors"] = errors
            self.results["exit_code"] = result.returncode

            # Parse metrics from output
            self._parse_output(output)

            # Check for errors
            if result.returncode != 0:
                self.results["status"] = "failed"
                self.results["errors"].append(f"Scraper exited with code {result.returncode}")
            elif errors:
                self.results["status"] = "warning"
                self.results["warnings"].append("Stderr output detected")
            else:
                self.results["status"] = "success"

            return result.returncode == 0

        except subprocess.TimeoutExpired:
            self.results["status"] = "timeout"
            self.results["errors"].append(f"Scraper timeout (>{timeout}s)")
            print(f"❌ ERROR: Scraper timeout after {timeout} seconds")
            return False

        except FileNotFoundError:
            self.results["status"] = "error"
            self.results["errors"].append("run_scraper.py not found")
            print("❌ ERROR: run_scraper.py not found")
            return False

        except Exception as e:
            self.results["status"] = "error"
            self.results["errors"].append(f"Unexpected error: {str(e)}")
            print(f"❌ ERROR: {e}")
            return False

    def _parse_output(self, output):
        """Parse scraper output for metrics"""
        # Extract press releases count
        press_match = re.search(r'Press releases:\s+(\d+)', output)
        if press_match:
            press_count = int(press_match.group(1))
            self.results["scrapers"]["press_releases"] = {
                "count": press_count,
                "status": "healthy" if press_count > 0 else "no_new_items"
            }
        else:
            self.results["scrapers"]["press_releases"] = {
                "count": 0,
                "status": "unknown"
            }

        # Extract votes count
        votes_match = re.search(r'Votes:\s+(\d+)', output)
        if votes_match:
            votes_count = int(votes_match.group(1))
            self.results["scrapers"]["votes"] = {
                "count": votes_count,
                "status": "healthy" if votes_count > 0 else "no_new_items"
            }
        else:
            self.results["scrapers"]["votes"] = {
                "count": 0,
                "status": "unknown"
            }

        # Extract total collected
        total_match = re.search(r'Total new items collected:\s+(\d+)', output)
        if total_match:
            self.results["metrics"]["total_collected"] = int(total_match.group(1))

        # Check for error indicators
        if "❌" in output or "Error" in output:
            error_lines = [line for line in output.split('\n') if "❌" in line or "Error" in line]
            self.results["errors"].extend(error_lines)

        # Check for archive failures
        if "Failed to archive" in output:
            self.results["warnings"].append("Some archive.org backups failed")

    def log_results(self):
        """Append results to JSONL log file"""
        try:
            with open(self.log_file, 'a') as f:
                json.dump(self.results, f)
                f.write('\n')
            print(f"✓ Results logged to {self.log_file}")
        except Exception as e:
            print(f"⚠ Failed to write log: {e}")

    def update_summary(self):
        """Update rolling summary statistics"""
        try:
            # Load existing summary
            if self.summary_file.exists():
                with open(self.summary_file, 'r') as f:
                    summary = json.load(f)
            else:
                summary = {
                    "total_runs": 0,
                    "successful_runs": 0,
                    "failed_runs": 0,
                    "last_success": None,
                    "last_failure": None,
                    "total_items_collected": 0,
                    "metrics_by_date": {}
                }

            # Update summary
            summary["total_runs"] += 1
            summary["last_run"] = self.results["timestamp"]

            if self.results["status"] == "success":
                summary["successful_runs"] += 1
                summary["last_success"] = self.results["timestamp"]
            else:
                summary["failed_runs"] += 1
                summary["last_failure"] = self.results["timestamp"]
                summary["last_error"] = self.results["errors"]

            # Update total collected
            if "total_collected" in self.results["metrics"]:
                summary["total_items_collected"] += self.results["metrics"]["total_collected"]

            # Update daily metrics
            date = self.results["date"]
            if date not in summary["metrics_by_date"]:
                summary["metrics_by_date"][date] = {
                    "runs": 0,
                    "items_collected": 0,
                    "press_releases": 0,
                    "votes": 0
                }

            summary["metrics_by_date"][date]["runs"] += 1

            if "total_collected" in self.results["metrics"]:
                summary["metrics_by_date"][date]["items_collected"] += self.results["metrics"]["total_collected"]

            if "press_releases" in self.results["scrapers"]:
                summary["metrics_by_date"][date]["press_releases"] += self.results["scrapers"]["press_releases"]["count"]

            if "votes" in self.results["scrapers"]:
                summary["metrics_by_date"][date]["votes"] += self.results["scrapers"]["votes"]["count"]

            # Calculate success rate
            summary["success_rate"] = f"{(summary['successful_runs'] / summary['total_runs'] * 100):.1f}%"

            # Save summary
            with open(self.summary_file, 'w') as f:
                json.dump(summary, f, indent=2)

            print(f"✓ Summary updated: {self.summary_file}")

        except Exception as e:
            print(f"⚠ Failed to update summary: {e}")

    def send_alert(self, message):
        """Send alert notification (placeholder for email/Slack)"""
        print("\n" + "!" * 80)
        print("ALERT: " + message)
        print("!" * 80)

        # Option 1: Send email via mailx (if configured)
        # subprocess.run(['mailx', '-s', 'Scraper Alert', 'your@email.com'],
        #                input=message.encode())

        # Option 2: Send to Slack webhook (if configured)
        # import requests
        # webhook_url = "https://hooks.slack.com/services/YOUR/WEBHOOK/URL"
        # requests.post(webhook_url, json={"text": message})

        # Option 3: Write to alert file
        alert_file = self.project_dir / "ALERTS.txt"
        try:
            with open(alert_file, 'a') as f:
                f.write(f"\n[{self.results['timestamp']}] {message}\n")
                if self.results.get("errors"):
                    f.write("Errors:\n")
                    for error in self.results["errors"]:
                        f.write(f"  - {error}\n")
        except Exception as e:
            print(f"Failed to write alert: {e}")

    def print_report(self):
        """Print human-readable report"""
        print("\n" + "=" * 80)
        print("SCRAPER MONITORING REPORT")
        print("=" * 80)
        print(f"Timestamp: {self.results['timestamp']}")
        print(f"Status: {self.results['status'].upper()}")
        print()

        # Scrapers
        print("Scrapers:")
        print("-" * 40)
        for scraper_name, scraper_data in self.results.get("scrapers", {}).items():
            status_icon = "✓" if scraper_data["status"] == "healthy" else "⚠"
            print(f"  {status_icon} {scraper_name}: {scraper_data['count']} items ({scraper_data['status']})")

        # Metrics
        if self.results.get("metrics"):
            print("\nMetrics:")
            print("-" * 40)
            for key, value in self.results["metrics"].items():
                print(f"  {key}: {value}")

        # Errors
        if self.results.get("errors"):
            print("\n❌ Errors:")
            print("-" * 40)
            for error in self.results["errors"]:
                print(f"  - {error}")

        # Warnings
        if self.results.get("warnings"):
            print("\n⚠ Warnings:")
            print("-" * 40)
            for warning in self.results["warnings"]:
                print(f"  - {warning}")

        print("=" * 80)

    def monitor(self):
        """Main monitoring workflow"""
        success = self.run_scraper()

        # Log results
        self.log_results()
        self.update_summary()

        # Print report
        self.print_report()

        # Send alerts on failure
        if not success or self.results["status"] in ["failed", "timeout", "error"]:
            alert_msg = f"Scraper {self.results['status']}: {', '.join(self.results['errors'])}"
            self.send_alert(alert_msg)

        # Warn if no new items collected for multiple runs
        if self.results.get("metrics", {}).get("total_collected", 0) == 0:
            print("\n⚠ Warning: No new items collected. This may be normal if no new content is available.")

        return success


def view_summary(project_dir=None):
    """View monitoring summary"""
    if project_dir is None:
        project_dir = Path(__file__).parent
    else:
        project_dir = Path(project_dir)

    summary_file = project_dir / "monitor_summary.json"

    if not summary_file.exists():
        print("No monitoring summary found. Run the monitor first.")
        return

    with open(summary_file, 'r') as f:
        summary = json.load(f)

    print("=" * 80)
    print("SCRAPER MONITORING SUMMARY")
    print("=" * 80)
    print(f"Total Runs: {summary['total_runs']}")
    print(f"Success Rate: {summary['success_rate']}")
    print(f"Successful: {summary['successful_runs']}")
    print(f"Failed: {summary['failed_runs']}")
    print(f"Total Items Collected: {summary['total_items_collected']}")
    print()

    if summary.get('last_success'):
        print(f"Last Success: {summary['last_success']}")

    if summary.get('last_failure'):
        print(f"Last Failure: {summary['last_failure']}")
        if summary.get('last_error'):
            print("  Errors:")
            for error in summary['last_error']:
                print(f"    - {error}")

    print("\nRecent Activity:")
    print("-" * 80)
    for date in sorted(summary.get('metrics_by_date', {}).keys(), reverse=True)[:7]:
        metrics = summary['metrics_by_date'][date]
        print(f"{date}: {metrics['items_collected']} items ({metrics['press_releases']} press, {metrics['votes']} votes) in {metrics['runs']} runs")

    print("=" * 80)


def view_logs(project_dir=None, lines=10):
    """View recent log entries"""
    if project_dir is None:
        project_dir = Path(__file__).parent
    else:
        project_dir = Path(project_dir)

    log_file = project_dir / "monitor_log.jsonl"

    if not log_file.exists():
        print("No log file found.")
        return

    print("=" * 80)
    print(f"RECENT LOG ENTRIES (last {lines})")
    print("=" * 80)

    with open(log_file, 'r') as f:
        log_lines = f.readlines()

    for line in log_lines[-lines:]:
        entry = json.loads(line)
        status_icon = {"success": "✓", "failed": "❌", "warning": "⚠", "timeout": "⏱", "error": "❌"}.get(entry["status"], "?")
        print(f"{status_icon} [{entry['timestamp']}] Status: {entry['status']}")

        if entry.get("metrics", {}).get("total_collected"):
            print(f"   Collected: {entry['metrics']['total_collected']} items")

        if entry.get("errors"):
            print(f"   Errors: {', '.join(entry['errors'][:3])}")

        print()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Monitor Langworthywatch scrapers")
    parser.add_argument('--summary', action='store_true', help='View monitoring summary')
    parser.add_argument('--logs', type=int, metavar='N', help='View last N log entries')
    parser.add_argument('--timeout', type=int, default=300, help='Scraper timeout in seconds')

    args = parser.parse_args()

    if args.summary:
        view_summary()
    elif args.logs:
        view_logs(lines=args.logs)
    else:
        # Run monitoring
        monitor = ScraperMonitor()
        success = monitor.monitor()
        sys.exit(0 if success else 1)
