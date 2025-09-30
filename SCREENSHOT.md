# Jira Viewer - Visual Preview

Since the application uses Tkinter GUI, here's a visual representation of what you'll see when running the application:

## Application Window

```
╔════════════════════════════════════════════════════════════════════════════╗
║                           Jira Ticket Viewer                                ║
╠════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║  Jira Server: [https://your-domain.atlassian.net         ] [Connect] ● Connected  ║
║                                                                             ║
╠════════════════════════════════════════════════════════════════════════════╣
║  ┌─ Search ──────────────────────────────────────────────────────────────┐ ║
║  │                                                                         │ ║
║  │  JQL Query: [project = PROJECT ORDER BY created DESC    ] [Search]    │ ║
║  │                                                            [Clear]     │ ║
║  │                                                                         │ ║
║  │  Quick Filters: [My Open Issues] [Recently Updated] [Recently Created] │ ║
║  │                                                                         │ ║
║  └─────────────────────────────────────────────────────────────────────────┘ ║
║                                                                             ║
║  ┌─ Results ──────────────────────────────────────────────────────────────┐ ║
║  │                                                                         │ ║
║  │  ┌──────────┬─────────────────────────┬──────────┬─────────┬────────┐  │ ║
║  │  │   Key    │        Summary          │  Status  │Assignee │Priority│  │ ║
║  │  ├──────────┼─────────────────────────┼──────────┼─────────┼────────┤  │ ║
║  │  │ PROJ-123 │ Fix login bug          │ Open     │ John    │ High   │  │ ║
║  │  │ PROJ-124 │ Add dashboard feature  │ Progress │ Sarah   │ Medium │  │ ║
║  │  │ PROJ-125 │ Update documentation   │ Review   │ Mike    │ Low    │  │ ║
║  │  │ PROJ-126 │ Implement API endpoint │ Open     │ Jane    │ High   │  │ ║
║  │  │ PROJ-127 │ Refactor database      │ Progress │ John    │ Medium │  │ ║
║  │  │          │                        │          │         │        │  │ ║
║  │  └──────────┴─────────────────────────┴──────────┴─────────┴────────┘  │ ║
║  │                                                                         │ ║
║  └─────────────────────────────────────────────────────────────────────────┘ ║
║                                                                             ║
║  ┌─ Issue Details ────────────────────────────────────────────────────────┐ ║
║  │                                                                         │ ║
║  │  [Open in Browser]  [Copy Key]                                         │ ║
║  │                                                                         │ ║
║  │  ┌───────────────────────────────────────────────────────────────────┐  │ ║
║  │  │ Key: PROJ-123                                                     │  │ ║
║  │  │ Summary: Fix login bug                                            │  │ ║
║  │  │ Status: Open                                                      │  │ ║
║  │  │ Priority: High                                                    │  │ ║
║  │  │ Assignee: John Doe                                                │  │ ║
║  │  │ Reporter: Jane Smith                                              │  │ ║
║  │  │ Created: 2024-01-15 10:30:00                                      │  │ ║
║  │  │ Updated: 2024-01-16 14:22:00                                      │  │ ║
║  │  │                                                                   │  │ ║
║  │  │ Description:                                                      │  │ ║
║  │  │ Users are unable to log in after the recent update. The login    │  │ ║
║  │  │ button becomes unresponsive when clicking. Need to investigate   │  │ ║
║  │  │ the authentication service and front-end validation.             │  │ ║
║  │  │                                                                   │  │ ║
║  │  │ Comments:                                                         │  │ ║
║  │  │ - Sarah (2024-01-16): I can reproduce this on staging            │  │ ║
║  │  │ - Mike (2024-01-16): Checking the logs now                       │  │ ║
║  │  └───────────────────────────────────────────────────────────────────┘  │ ║
║  │                                                                         │ ║
║  └─────────────────────────────────────────────────────────────────────────┘ ║
║                                                                             ║
╚════════════════════════════════════════════════════════════════════════════╝
```

## UI Components Explained

### 1. Connection Bar (Top)
- **Server URL Field**: Enter or modify your Jira instance URL
- **Connect Button**: Establish connection to Jira
- **Status Indicator**: Shows connection status with color coding
  - 🔴 Red: Not connected / Connection failed
  - 🟠 Orange: No credentials configured
  - 🟢 Green: Successfully connected

### 2. Search Section
- **JQL Query Field**: Enter custom JQL queries
  - Press Enter to execute search
  - Pre-filled with example query
- **Search Button**: Execute the query
- **Clear Button**: Clear all results and details

### 3. Quick Filters
Three one-click buttons for common searches:
- **My Open Issues**: `assignee = currentUser() AND resolution = Unresolved`
- **Recently Updated**: `updated >= -7d ORDER BY updated DESC`
- **Recently Created**: `created >= -7d ORDER BY created DESC`

### 4. Results Table
Displays search results in a scrollable table:
- **Key**: Click to select, double-click to view details
- **Summary**: Issue title/description
- **Status**: Current workflow status
- **Assignee**: Person responsible
- **Priority**: Issue priority level

### 5. Details Panel
Shows comprehensive issue information:
- **Action Buttons**:
  - Open in Browser: Opens issue in default web browser
  - Copy Key: Copies issue key to clipboard
- **Detail View**:
  - All issue fields
  - Full description
  - Recent comments (last 5)

## Color Scheme
The application uses the default system theme with:
- Clean, professional layout
- High contrast for readability
- Intuitive button placement
- Responsive design

## Window Properties
- **Default Size**: 1200x800 pixels
- **Resizable**: Yes
- **Minimum Size**: Not enforced (can be adjusted)
- **Platform**: Works on Windows, macOS, and Linux

## Interaction Methods
1. **Keyboard**: 
   - Enter key in search field executes search
   - Tab to navigate between fields
   
2. **Mouse**:
   - Single click to select items
   - Double click to view details
   - Click buttons for actions

3. **Scroll**:
   - Mouse wheel or scrollbar for results
   - Scrollbar for issue details

## Visual Feedback
- Message boxes for success/error notifications
- Status indicator color changes
- Result count displayed on search completion
- Immediate UI updates on actions

---

**Note**: The actual application uses native Tkinter widgets which will match your operating system's look and feel. The above is a representation of the layout and structure.

To see the real application, run:
```bash
python jira_viewer.py
```
