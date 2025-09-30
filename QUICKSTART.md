# Quick Start Guide

Get up and running with Jira Viewer in 5 minutes!

## Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 2: Configure Credentials

1. Copy the example environment file:
```bash
cp .env.example .env
```

2. Edit `.env` and add your Jira credentials:
```env
JIRA_SERVER=https://your-company.atlassian.net
JIRA_USERNAME=your-email@example.com
JIRA_API_TOKEN=your-api-token
```

> **Getting an API Token:**
> Visit https://id.atlassian.com/manage-profile/security/api-tokens and create a new token.

## Step 3: Run the Application

```bash
python jira_viewer.py
```

## Step 4: Search for Tickets

1. The app will connect to your Jira instance automatically
2. Enter a JQL query in the search box (or use a Quick Filter)
3. Click Search or press Enter
4. Double-click any ticket to view details

## Example Queries

**Your open tickets:**
```jql
assignee = currentUser() AND resolution = Unresolved
```

**Recent high-priority issues:**
```jql
priority = High AND created >= -7d
```

**Issues in a specific project:**
```jql
project = "YOUR_PROJECT_KEY"
```

## Common Issues

**Connection Error?**
- Verify your server URL is correct
- Check that your API token is valid
- Ensure you have internet connectivity

**No results?**
- Check your JQL syntax
- Verify you have permission to view the project
- Try a simpler query first

## Need Help?

- See [README.md](README.md) for detailed documentation
- See [UI_OVERVIEW.md](UI_OVERVIEW.md) for interface details
- Run `python example_usage.py` for API examples
- Run `python test_setup.py` to validate your setup
