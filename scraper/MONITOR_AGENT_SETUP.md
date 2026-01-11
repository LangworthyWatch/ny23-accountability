# Scraper Monitor Agent Setup Guide

## Overview

The scraper monitor agent provides automated monitoring and alerting for the Langworthywatch scrapers:
- Runs scrapers on schedule
- Tracks success/failure rates
- Logs detailed metrics
- Sends alerts on failures
- Maintains historical statistics

## Quick Start

### 1. Test the Monitor

```bash
cd /Users/zachbeaudoin/Langworthywatch/scraper
python3 monitor_agent.py
```

This will:
- Run `run_scraper.py`
- Parse output for metrics
- Log results to `monitor_log.jsonl`
- Update summary statistics in `monitor_summary.json`
- Display a detailed report

### 2. View Summary Statistics

```bash
python3 monitor_agent.py --summary
```

Shows:
- Total runs and success rate
- Total items collected
- Last success/failure timestamps
- Recent activity by date

### 3. View Recent Logs

```bash
# View last 10 log entries
python3 monitor_agent.py --logs 10

# View last 50 entries
python3 monitor_agent.py --logs 50
```

## Scheduling

### Option A: Cron (macOS/Linux)

Run every 6 hours:

```bash
crontab -e
```

Add:
```
0 */6 * * * cd /Users/zachbeaudoin/Langworthywatch/scraper && /usr/bin/python3 monitor_agent.py >> monitor.log 2>&1
```

Run daily at 6 AM:
```
0 6 * * * cd /Users/zachbeaudoin/Langworthywatch/scraper && /usr/bin/python3 monitor_agent.py >> monitor.log 2>&1
```

### Option B: launchd (macOS recommended)

Create `/Users/zachbeaudoin/Library/LaunchAgents/com.langworthywatch.scraper.plist`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.langworthywatch.scraper</string>

    <key>ProgramArguments</key>
    <array>
        <string>/usr/bin/python3</string>
        <string>/Users/zachbeaudoin/Langworthywatch/scraper/monitor_agent.py</string>
    </array>

    <key>WorkingDirectory</key>
    <string>/Users/zachbeaudoin/Langworthywatch/scraper</string>

    <key>StartInterval</key>
    <integer>21600</integer> <!-- 6 hours in seconds -->

    <key>StandardOutPath</key>
    <string>/Users/zachbeaudoin/Langworthywatch/scraper/monitor.log</string>

    <key>StandardErrorPath</key>
    <string>/Users/zachbeaudoin/Langworthywatch/scraper/monitor_error.log</string>

    <key>RunAtLoad</key>
    <true/>
</dict>
</plist>
```

Load and start:
```bash
launchctl load ~/Library/LaunchAgents/com.langworthywatch.scraper.plist
launchctl start com.langworthywatch.scraper
```

Check status:
```bash
launchctl list | grep langworthywatch
```

## Alert Configuration

The monitor includes three alert options. Uncomment and configure your preferred method in `monitor_agent.py`:

### Option A: Email (via mailx)

```python
def send_alert(self, message):
    import subprocess
    subprocess.run(
        ['mailx', '-s', 'Langworthywatch Scraper Alert', 'your@email.com'],
        input=message.encode()
    )
```

Setup mailx on macOS:
```bash
brew install mailutils
# Configure SMTP settings in ~/.mailrc
```

### Option B: Slack Webhook

```python
def send_alert(self, message):
    import requests
    webhook_url = "https://hooks.slack.com/services/YOUR/WEBHOOK/URL"
    payload = {
        "text": f"🚨 Scraper Alert: {message}",
        "username": "Langworthywatch Monitor",
        "icon_emoji": ":rotating_light:"
    }
    requests.post(webhook_url, json=payload)
```

Setup Slack webhook:
1. Go to https://api.slack.com/messaging/webhooks
2. Create incoming webhook
3. Copy webhook URL
4. Update `webhook_url` in code

### Option C: Discord Webhook

```python
def send_alert(self, message):
    import requests
    webhook_url = "https://discord.com/api/webhooks/YOUR/WEBHOOK"
    payload = {
        "content": f"🚨 **Scraper Alert**\n{message}"
    }
    requests.post(webhook_url, json=payload)
```

## Monitoring Metrics

The monitor tracks:

### Per-Run Metrics
- **Timestamp**: When the scraper ran
- **Status**: success, failed, timeout, error
- **Press releases collected**: Number of new press releases
- **Votes collected**: Number of new votes
- **Total collected**: Combined count
- **Errors**: Error messages if any
- **Warnings**: Non-fatal issues
- **Exit code**: Scraper process exit code

### Summary Statistics
- **Total runs**: All-time run count
- **Success rate**: Percentage of successful runs
- **Total items collected**: All-time collection count
- **Last success/failure**: Timestamps
- **Daily metrics**: Items collected per day

## File Locations

```
/Users/zachbeaudoin/Langworthywatch/scraper/
├── monitor_agent.py           # Main monitor script
├── monitor_log.jsonl          # Detailed logs (append-only)
├── monitor_summary.json       # Rolling summary statistics
├── ALERTS.txt                 # Alert history
├── monitor.log                # Cron/launchd stdout
└── monitor_error.log          # Cron/launchd stderr
```

## Log Format

### monitor_log.jsonl
Each line is a JSON object:
```json
{
  "timestamp": "2025-01-06T15:30:00",
  "date": "2025-01-06",
  "time": "15:30:00",
  "status": "success",
  "scrapers": {
    "press_releases": {"count": 3, "status": "healthy"},
    "votes": {"count": 2, "status": "healthy"}
  },
  "metrics": {"total_collected": 5},
  "errors": [],
  "warnings": []
}
```

### monitor_summary.json
Rolling statistics:
```json
{
  "total_runs": 42,
  "successful_runs": 40,
  "failed_runs": 2,
  "success_rate": "95.2%",
  "total_items_collected": 127,
  "last_success": "2025-01-06T15:30:00",
  "last_run": "2025-01-06T15:30:00",
  "metrics_by_date": {
    "2025-01-06": {
      "runs": 2,
      "items_collected": 5,
      "press_releases": 3,
      "votes": 2
    }
  }
}
```

## Troubleshooting

### "run_scraper.py not found"

```bash
# Verify you're in the correct directory
cd /Users/zachbeaudoin/Langworthywatch/scraper
ls -la run_scraper.py

# Run monitor from scraper directory
python3 monitor_agent.py
```

### Timeout errors

Increase timeout (default 300s = 5min):

```bash
python3 monitor_agent.py --timeout 600
```

Or edit `monitor_agent.py`:
```python
result = subprocess.run(..., timeout=600)  # 10 minutes
```

### Cron job not running

```bash
# Check cron is running
ps aux | grep cron

# View cron logs (macOS)
log show --predicate 'eventMessage contains "cron"' --last 1d

# Test with simple cron entry
* * * * * date >> /tmp/cron-test.txt
```

### No alerts being sent

1. Check `ALERTS.txt` is being written:
   ```bash
   cat /Users/zachbeaudoin/Langworthywatch/scraper/ALERTS.txt
   ```

2. Trigger a test alert:
   ```bash
   # Temporarily break the scraper to test alerts
   mv run_scraper.py run_scraper.py.backup
   python3 monitor_agent.py
   mv run_scraper.py.backup run_scraper.py
   ```

3. Verify alert method is configured (email/Slack/Discord)

### Empty logs

```bash
# Check file permissions
ls -la monitor_log.jsonl

# Test manual write
echo 'test' >> monitor_log.jsonl

# Run monitor with verbose output
python3 -v monitor_agent.py
```

## Integration with GitHub Actions

Add `.github/workflows/scraper-monitor.yml`:

```yaml
name: Scraper Monitor

on:
  schedule:
    - cron: '0 */6 * * *'  # Every 6 hours
  workflow_dispatch:  # Manual trigger

jobs:
  monitor:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          cd scraper
          pip install -r requirements.txt

      - name: Run monitor
        run: |
          cd scraper
          python monitor_agent.py

      - name: Upload logs
        if: always()
        uses: actions/upload-artifact@v3
        with:
          name: monitor-logs
          path: scraper/monitor_*.json*

      - name: Notify on failure
        if: failure()
        run: |
          # Send notification
          echo "Scraper monitoring failed!"
```

## Best Practices

1. **Test first**: Run manually before scheduling
2. **Check logs weekly**: Review `monitor_summary.json`
3. **Set up alerts**: Configure email/Slack for failures
4. **Monitor disk usage**: Log files grow over time
5. **Rotate logs**: Archive old logs monthly

## Log Rotation

Add to weekly cron:

```bash
# Rotate logs weekly
0 0 * * 0 cd /Users/zachbeaudoin/Langworthywatch/scraper && gzip monitor_log.jsonl && mv monitor_log.jsonl.gz "monitor_log_$(date +\%Y\%m\%d).jsonl.gz" && touch monitor_log.jsonl
```

Or create `/Users/zachbeaudoin/Langworthywatch/scraper/rotate_logs.sh`:

```bash
#!/bin/bash
cd /Users/zachbeaudoin/Langworthywatch/scraper

# Archive logs older than 30 days
find . -name "monitor_log_*.jsonl.gz" -mtime +30 -delete

# Compress current log if > 10MB
if [ $(stat -f%z monitor_log.jsonl) -gt 10485760 ]; then
    gzip monitor_log.jsonl
    mv monitor_log.jsonl.gz "monitor_log_$(date +%Y%m%d).jsonl.gz"
    touch monitor_log.jsonl
fi
```

## Next Steps

After setting up the scraper monitor:

1. Configure alert notifications
2. Set up scheduled runs (cron/launchd)
3. Test failure scenarios
4. Monitor for 1 week and adjust schedule as needed
5. Consider implementing the Fact-Checking Validation Agent next

---

For questions or issues, check the logs first:
```bash
python3 monitor_agent.py --summary
python3 monitor_agent.py --logs 20
```
