# Step-by-Step Usage Guide

This guide walks you through using the Jira Viewer application with detailed instructions.

## Step 1: First Launch

When you first run `python jira_viewer.py`, you'll see:

1. **Connection Bar** (top of window)
   - Server URL field (pre-filled from .env or default)
   - Connect button
   - Status indicator (shows "Not connected" in red initially)

2. **Search Section**
   - JQL Query input field (pre-filled with example query)
   - Search button
   - Clear button

3. **Quick Filters** (below search)
   - Three quick access buttons for common searches

4. **Results Area** (middle section)
   - Empty table with column headers (Key, Summary, Status, Assignee, Priority)

5. **Details Panel** (bottom section)
   - Action buttons (Open in Browser, Copy Key)
   - Empty text area for issue details

## Step 2: Connecting to Jira

### If you have credentials configured in .env:
- The app automatically attempts to connect on startup
- If successful: Status changes to "Connected" (green)
- If failed: Error dialog appears with details

### If you need to change the server:
1. Edit the Server URL field
2. Click "Connect" button
3. Wait for connection confirmation

### Connection Status Indicators:
- 🔴 Red "Not connected" - No connection
- 🟠 Orange "No credentials" - Missing username/token
- 🔴 Red "Connection failed" - Connection error
- 🟢 Green "Connected" - Successfully connected

## Step 3: Searching for Issues

### Using Quick Filters:
1. Click any Quick Filter button:
   - **My Open Issues**: Shows your unresolved tasks
   - **Recently Updated**: Shows issues updated in last 7 days
   - **Recently Created**: Shows issues created in last 7 days

2. Query auto-fills in the search box
3. Search executes automatically
4. Results appear in the table

### Using Custom JQL:
1. Click in the JQL Query field
2. Type or modify your query
3. Press Enter OR click "Search" button

### Example Queries You Can Try:

**By Project:**
```
project = "MYPROJECT"
```

**By Status:**
```
status = "In Progress"
```

**By Priority:**
```
priority = High
```

**By Assignee:**
```
assignee = "john.doe@company.com"
```

**Complex Query:**
```
project = "MYPROJECT" AND status != Done AND priority IN (High, Highest) ORDER BY created DESC
```

## Step 4: Viewing Search Results

Results appear in the table with these columns:

1. **Key** - Issue identifier (e.g., PROJ-123)
2. **Summary** - Issue title/description
3. **Status** - Current status (Open, In Progress, Done, etc.)
4. **Assignee** - Person assigned to the issue
5. **Priority** - Priority level (High, Medium, Low, etc.)

### Navigation:
- Scroll through results using scrollbar
- Click column headers to view data
- Double-click any row to see details

## Step 5: Viewing Issue Details

When you double-click an issue:

1. **Details Panel Updates** with:
   - Issue Key
   - Summary
   - Status and Priority
   - Assignee and Reporter
   - Created and Updated timestamps
   - Full Description
   - Recent Comments (last 5)

2. **Scroll** to read full details

3. **Use Action Buttons**:

## Step 6: Taking Actions

### Open in Browser:
1. Select an issue (single click on row)
2. Click "Open in Browser"
3. Your default browser opens to the issue page

### Copy Issue Key:
1. Select an issue
2. Click "Copy Key"
3. Confirmation dialog appears
4. Paste the key anywhere (Ctrl+V / Cmd+V)

## Step 7: Managing Results

### Clear Results:
- Click "Clear" button to:
  - Remove all results from table
  - Clear the details panel
  - Keep your query for editing

### New Search:
- Enter new query
- Click Search
- Previous results are replaced

## Tips & Tricks

### Keyboard Shortcuts:
- **Enter** in query field → Execute search
- **Ctrl+A** in results → Select (for copy operations)

### Efficient Workflows:

**Daily Standup Preparation:**
1. Quick Filter: "My Open Issues"
2. Review list
3. Double-click each for details

**Bug Triage:**
```jql
project = MYPROJECT AND type = Bug AND status = Open ORDER BY priority DESC
```

**Sprint Planning:**
```jql
project = MYPROJECT AND sprint is EMPTY AND status != Done ORDER BY priority DESC
```

**Finding Blockers:**
```jql
status = "In Progress" AND priority = Blocker
```

### Working with Multiple Searches:
1. Execute first search
2. Copy important issue keys
3. Execute second search
4. Compare results

### Understanding JQL:
- `AND` - Both conditions must be true
- `OR` - Either condition can be true
- `!=` - Not equal to
- `IN (value1, value2)` - Matches any value
- `ORDER BY` - Sort results
- `DESC` - Descending order
- `ASC` - Ascending order

## Troubleshooting Common Issues

### "Connection Failed"
1. Check internet connection
2. Verify server URL (must start with https://)
3. Confirm API token is valid
4. Check username is correct

### "No Results Found"
1. Verify your JQL syntax
2. Check you have access to the project
3. Try a simpler query first
4. Verify issues exist matching criteria

### "Search Error"
1. Review JQL syntax (check for typos)
2. Ensure field names are correct
3. Verify you're using valid operators
4. Check date formats if using dates

### Application Won't Start
1. Verify Python 3.7+ is installed
2. Run: `pip install -r requirements.txt`
3. Check for error messages
4. Run: `python test_setup.py`

## Advanced Usage

### Programmatic Access:
See `example_usage.py` for API examples

### Custom Integration:
The `jira_viewer.py` module can be imported:
```python
from jira_viewer import JiraViewer
# Use in your own scripts
```

### Automation:
Create scripts that use the Jira library directly for automated workflows

---

**Need More Help?**
- See [README.md](README.md) for installation
- See [QUICKSTART.md](QUICKSTART.md) for quick setup
- See [CONTRIBUTING.md](CONTRIBUTING.md) to help improve this tool
