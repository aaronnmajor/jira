# Jira Ticket Viewer

A simple and easy-to-use GUI application for searching and viewing Jira tickets. Built with Python and Tkinter, this tool provides a user-friendly interface to interact with your Jira instance.

## Features

- 🔍 **Search Jira tickets** using JQL (Jira Query Language)
- 📋 **View search results** in an organized table format
- 📝 **View detailed information** about each ticket
- ⚡ **Quick filter buttons** for common searches
- 🌐 **Open tickets in browser** directly from the app
- 📋 **Copy ticket keys** to clipboard
- 🔐 **Secure credential management** using environment variables

## Documentation

- 📖 [Quick Start Guide](QUICKSTART.md) - Get started in 5 minutes
- 🎨 [UI Overview](UI_OVERVIEW.md) - Visual guide to the interface
- 🤝 [Contributing Guide](CONTRIBUTING.md) - How to contribute to the project

## Prerequisites

- Python 3.7 or higher
- A Jira account with API access
- Jira API token (see setup instructions below)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/aaronnmajor/jira.git
cd jira
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your Jira credentials:
   - Copy `.env.example` to `.env`
   - Edit `.env` and fill in your Jira credentials:
     ```
     JIRA_SERVER=https://your-domain.atlassian.net
     JIRA_USERNAME=your-email@example.com
     JIRA_API_TOKEN=your-api-token-here
     ```

### Getting Your Jira API Token

1. Log in to your Atlassian account
2. Go to [https://id.atlassian.com/manage-profile/security/api-tokens](https://id.atlassian.com/manage-profile/security/api-tokens)
3. Click "Create API token"
4. Give it a label (e.g., "Jira Viewer App")
5. Copy the token and paste it into your `.env` file

## Usage

Run the application:
```bash
python jira_viewer.py
```

### Main Features

#### Connecting to Jira
1. The app will automatically try to connect using credentials from your `.env` file
2. You can also enter the server URL manually and click "Connect"

#### Searching for Tickets
1. Enter a JQL query in the search box
2. Click "Search" or press Enter
3. Results will appear in the table below

#### Using Quick Filters
Use the quick filter buttons for common searches:
- **My Open Issues**: Shows all unresolved issues assigned to you
- **Recently Updated**: Shows issues updated in the last 7 days
- **Recently Created**: Shows issues created in the last 7 days

#### Viewing Ticket Details
- Double-click any ticket in the results table to view full details
- Details include: summary, status, priority, assignee, description, and recent comments

#### Opening Tickets in Browser
- Select a ticket and click "Open in Browser" to view it in your default web browser

#### Copying Ticket Keys
- Select a ticket and click "Copy Key" to copy the ticket key to your clipboard

### Example JQL Queries

Here are some useful JQL queries to get you started:

```jql
# All open issues assigned to you
assignee = currentUser() AND resolution = Unresolved

# High priority bugs
type = Bug AND priority = High

# Issues in a specific project
project = "PROJECT_KEY"

# Issues created in the last week
created >= -7d ORDER BY created DESC

# Issues with specific status
status = "In Progress"

# Complex query
project = "PROJECT_KEY" AND status != Done AND assignee = currentUser() ORDER BY priority DESC
```

For more information on JQL, see the [Atlassian JQL documentation](https://support.atlassian.com/jira-service-management-cloud/docs/use-advanced-search-with-jira-query-language-jql/).

## Troubleshooting

### Connection Issues
- Verify your Jira server URL is correct (should include `https://`)
- Check that your API token is valid
- Ensure your username is correct (usually your email)
- Make sure you have the necessary permissions in Jira

### Search Issues
- Verify your JQL syntax is correct
- Check that you have permission to view the projects in your query
- Try a simpler query to test connectivity

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Security Note

⚠️ **Never commit your `.env` file to version control!** The `.gitignore` file is configured to exclude it, but always double-check before committing.