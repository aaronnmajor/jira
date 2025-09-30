## User Interface Overview

The Jira Viewer provides a clean and intuitive interface:

```
┌─────────────────────────────────────────────────────────────────────┐
│ Jira Ticket Viewer                                                  │
├─────────────────────────────────────────────────────────────────────┤
│ Jira Server: [https://your-domain.atlassian.net] [Connect] ● Not   │
│                                                                 connected
├─────────────────────────────────────────────────────────────────────┤
│ Search                                                              │
│ JQL Query: [project = PROJECT ORDER BY created DESC    ] [Search]  │
│                                                           [Clear]   │
│ Quick Filters: [My Open Issues] [Recently Updated] [Recently Created]│
├─────────────────────────────────────────────────────────────────────┤
│ Results                                                             │
│ ┌─────────┬───────────────────┬──────────┬──────────┬──────────┐   │
│ │ Key     │ Summary           │ Status   │ Assignee │ Priority │   │
│ ├─────────┼───────────────────┼──────────┼──────────┼──────────┤   │
│ │ PROJ-123│ Fix login bug     │ Open     │ John Doe │ High     │   │
│ │ PROJ-124│ Add new feature   │ In Prog. │ Jane Smith│ Medium  │   │
│ │ PROJ-125│ Update docs       │ Done     │ Unassigned│ Low     │   │
│ └─────────┴───────────────────┴──────────┴──────────┴──────────┘   │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│ Issue Details                                                       │
│ [Open in Browser] [Copy Key]                                       │
│ ┌───────────────────────────────────────────────────────────────┐   │
│ │ Key: PROJ-123                                                 │   │
│ │ Summary: Fix login bug                                        │   │
│ │ Status: Open                                                  │   │
│ │ Priority: High                                                │   │
│ │ Assignee: John Doe                                            │   │
│ │ Reporter: Jane Smith                                          │   │
│ │ Created: 2024-01-15 10:30:00                                  │   │
│ │ Updated: 2024-01-16 14:22:00                                  │   │
│ │                                                               │   │
│ │ Description:                                                  │   │
│ │ Users are unable to log in after the recent update...        │   │
│ └───────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
```

### UI Components

1. **Connection Bar**: Configure and connect to your Jira instance
2. **Search Section**: Enter JQL queries and execute searches
3. **Quick Filters**: One-click access to common search queries
4. **Results Table**: View search results in a sortable table format
5. **Details Panel**: View comprehensive information about selected tickets
6. **Action Buttons**: Open tickets in browser or copy ticket keys
