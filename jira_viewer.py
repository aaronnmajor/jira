#!/usr/bin/env python3
"""
Jira Ticket Viewer - A simple GUI application to search and view Jira tickets.
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import os
from dotenv import load_dotenv
from jira import JIRA
import webbrowser

# Load environment variables
load_dotenv()


class JiraViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Jira Ticket Viewer")
        self.root.geometry("1200x800")
        
        self.jira = None
        self.current_issues = []
        
        # Create UI
        self.create_widgets()
        
        # Try to connect to Jira on startup
        self.connect_jira()
    
    def create_widgets(self):
        # Top frame for connection info
        top_frame = ttk.Frame(self.root, padding="10")
        top_frame.pack(fill=tk.X)
        
        ttk.Label(top_frame, text="Jira Server:").pack(side=tk.LEFT, padx=5)
        self.server_var = tk.StringVar(value=os.getenv('JIRA_SERVER', 'https://your-domain.atlassian.net'))
        ttk.Entry(top_frame, textvariable=self.server_var, width=40).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(top_frame, text="Connect", command=self.connect_jira).pack(side=tk.LEFT, padx=5)
        
        self.status_label = ttk.Label(top_frame, text="Not connected", foreground="red")
        self.status_label.pack(side=tk.LEFT, padx=10)
        
        # Search frame
        search_frame = ttk.LabelFrame(self.root, text="Search", padding="10")
        search_frame.pack(fill=tk.X, padx=10, pady=5)
        
        ttk.Label(search_frame, text="JQL Query:").pack(side=tk.LEFT, padx=5)
        self.query_var = tk.StringVar(value="project = PROJECT ORDER BY created DESC")
        self.query_entry = ttk.Entry(search_frame, textvariable=self.query_var, width=60)
        self.query_entry.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        self.query_entry.bind('<Return>', lambda e: self.search_issues())
        
        ttk.Button(search_frame, text="Search", command=self.search_issues).pack(side=tk.LEFT, padx=5)
        ttk.Button(search_frame, text="Clear", command=self.clear_results).pack(side=tk.LEFT, padx=5)
        
        # Quick filters frame
        quick_filter_frame = ttk.Frame(self.root, padding="5")
        quick_filter_frame.pack(fill=tk.X, padx=10)
        
        ttk.Label(quick_filter_frame, text="Quick Filters:").pack(side=tk.LEFT, padx=5)
        ttk.Button(quick_filter_frame, text="My Open Issues", 
                  command=lambda: self.set_query("assignee = currentUser() AND resolution = Unresolved ORDER BY updated DESC")).pack(side=tk.LEFT, padx=2)
        ttk.Button(quick_filter_frame, text="Recently Updated", 
                  command=lambda: self.set_query("updated >= -7d ORDER BY updated DESC")).pack(side=tk.LEFT, padx=2)
        ttk.Button(quick_filter_frame, text="Recently Created", 
                  command=lambda: self.set_query("created >= -7d ORDER BY created DESC")).pack(side=tk.LEFT, padx=2)
        
        # Results frame with scrollbar
        results_frame = ttk.LabelFrame(self.root, text="Results", padding="10")
        results_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Create Treeview for results
        tree_scroll = ttk.Scrollbar(results_frame)
        tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.results_tree = ttk.Treeview(results_frame, 
                                        columns=('key', 'summary', 'status', 'assignee', 'priority'),
                                        show='headings',
                                        yscrollcommand=tree_scroll.set)
        tree_scroll.config(command=self.results_tree.yview)
        
        # Define columns
        self.results_tree.heading('key', text='Key')
        self.results_tree.heading('summary', text='Summary')
        self.results_tree.heading('status', text='Status')
        self.results_tree.heading('assignee', text='Assignee')
        self.results_tree.heading('priority', text='Priority')
        
        self.results_tree.column('key', width=100)
        self.results_tree.column('summary', width=400)
        self.results_tree.column('status', width=100)
        self.results_tree.column('assignee', width=150)
        self.results_tree.column('priority', width=80)
        
        self.results_tree.pack(fill=tk.BOTH, expand=True)
        self.results_tree.bind('<Double-1>', self.show_issue_details)
        
        # Details frame
        details_frame = ttk.LabelFrame(self.root, text="Issue Details", padding="10")
        details_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Create a frame for buttons
        button_frame = ttk.Frame(details_frame)
        button_frame.pack(fill=tk.X, pady=(0, 5))
        
        ttk.Button(button_frame, text="Open in Browser", command=self.open_in_browser).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Copy Key", command=self.copy_key).pack(side=tk.LEFT, padx=5)
        
        self.details_text = scrolledtext.ScrolledText(details_frame, height=10, wrap=tk.WORD)
        self.details_text.pack(fill=tk.BOTH, expand=True)
        
    def connect_jira(self):
        """Connect to Jira server"""
        server = self.server_var.get()
        username = os.getenv('JIRA_USERNAME', '')
        api_token = os.getenv('JIRA_API_TOKEN', '')
        
        if not server:
            messagebox.showerror("Error", "Please provide Jira server URL")
            return
        
        if not username or not api_token:
            messagebox.showwarning("Warning", 
                                 "JIRA_USERNAME and JIRA_API_TOKEN not found in environment.\n"
                                 "Please create a .env file with these credentials.\n\n"
                                 "Connection will fail without valid credentials.")
            self.status_label.config(text="No credentials", foreground="orange")
            return
        
        try:
            self.jira = JIRA(server=server, basic_auth=(username, api_token))
            self.status_label.config(text="Connected", foreground="green")
            messagebox.showinfo("Success", "Connected to Jira successfully!")
        except Exception as e:
            self.status_label.config(text="Connection failed", foreground="red")
            messagebox.showerror("Connection Error", f"Failed to connect to Jira:\n{str(e)}")
    
    def set_query(self, query):
        """Set the JQL query"""
        self.query_var.set(query)
        self.search_issues()
    
    def search_issues(self):
        """Search for issues using JQL query"""
        if not self.jira:
            messagebox.showerror("Error", "Please connect to Jira first")
            return
        
        query = self.query_var.get()
        if not query:
            messagebox.showerror("Error", "Please enter a JQL query")
            return
        
        try:
            # Clear previous results
            self.clear_results()
            
            # Search for issues
            issues = self.jira.search_issues(query, maxResults=100)
            self.current_issues = issues
            
            # Display results
            for issue in issues:
                assignee = getattr(issue.fields.assignee, 'displayName', 'Unassigned') if issue.fields.assignee else 'Unassigned'
                priority = getattr(issue.fields.priority, 'name', 'None') if issue.fields.priority else 'None'
                
                self.results_tree.insert('', tk.END, values=(
                    issue.key,
                    issue.fields.summary,
                    issue.fields.status.name,
                    assignee,
                    priority
                ))
            
            messagebox.showinfo("Search Complete", f"Found {len(issues)} issue(s)")
        except Exception as e:
            messagebox.showerror("Search Error", f"Failed to search issues:\n{str(e)}")
    
    def clear_results(self):
        """Clear the results tree"""
        for item in self.results_tree.get_children():
            self.results_tree.delete(item)
        self.details_text.delete(1.0, tk.END)
        self.current_issues = []
    
    def show_issue_details(self, event):
        """Show details of selected issue"""
        selection = self.results_tree.selection()
        if not selection:
            return
        
        # Get selected item
        item = self.results_tree.item(selection[0])
        key = item['values'][0]
        
        # Find the issue
        issue = None
        for iss in self.current_issues:
            if iss.key == key:
                issue = iss
                break
        
        if not issue:
            return
        
        # Display details
        self.details_text.delete(1.0, tk.END)
        
        details = f"Key: {issue.key}\n"
        details += f"Summary: {issue.fields.summary}\n"
        details += f"Status: {issue.fields.status.name}\n"
        details += f"Priority: {getattr(issue.fields.priority, 'name', 'None') if issue.fields.priority else 'None'}\n"
        details += f"Assignee: {getattr(issue.fields.assignee, 'displayName', 'Unassigned') if issue.fields.assignee else 'Unassigned'}\n"
        details += f"Reporter: {getattr(issue.fields.reporter, 'displayName', 'Unknown') if issue.fields.reporter else 'Unknown'}\n"
        details += f"Created: {issue.fields.created}\n"
        details += f"Updated: {issue.fields.updated}\n"
        
        if hasattr(issue.fields, 'description') and issue.fields.description:
            details += f"\nDescription:\n{issue.fields.description}\n"
        
        if hasattr(issue.fields, 'comment') and issue.fields.comment.comments:
            details += f"\nComments ({len(issue.fields.comment.comments)}):\n"
            for comment in issue.fields.comment.comments[:5]:  # Show last 5 comments
                author = getattr(comment.author, 'displayName', 'Unknown')
                details += f"\n{author} ({comment.created}):\n{comment.body}\n"
        
        self.details_text.insert(1.0, details)
    
    def open_in_browser(self):
        """Open selected issue in browser"""
        selection = self.results_tree.selection()
        if not selection:
            messagebox.showwarning("Warning", "Please select an issue first")
            return
        
        item = self.results_tree.item(selection[0])
        key = item['values'][0]
        server = self.server_var.get()
        url = f"{server}/browse/{key}"
        webbrowser.open(url)
    
    def copy_key(self):
        """Copy selected issue key to clipboard"""
        selection = self.results_tree.selection()
        if not selection:
            messagebox.showwarning("Warning", "Please select an issue first")
            return
        
        item = self.results_tree.item(selection[0])
        key = item['values'][0]
        self.root.clipboard_clear()
        self.root.clipboard_append(key)
        messagebox.showinfo("Copied", f"Issue key {key} copied to clipboard")


def main():
    root = tk.Tk()
    app = JiraViewer(root)
    root.mainloop()


if __name__ == "__main__":
    main()
