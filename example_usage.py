#!/usr/bin/env python3
"""
Example: Programmatic usage of Jira API
This script demonstrates how to use the Jira library directly for automation tasks.
"""

import os
from dotenv import load_dotenv
from jira import JIRA

# Load environment variables
load_dotenv()

def connect_to_jira():
    """Connect to Jira instance"""
    server = os.getenv('JIRA_SERVER')
    username = os.getenv('JIRA_USERNAME')
    api_token = os.getenv('JIRA_API_TOKEN')
    
    if not all([server, username, api_token]):
        print("Error: Missing Jira credentials in .env file")
        print("Please copy .env.example to .env and fill in your credentials")
        return None
    
    try:
        jira = JIRA(server=server, basic_auth=(username, api_token))
        print(f"✓ Connected to Jira: {server}")
        return jira
    except Exception as e:
        print(f"✗ Failed to connect: {e}")
        return None

def search_issues(jira, jql_query, max_results=10):
    """Search for issues using JQL"""
    try:
        issues = jira.search_issues(jql_query, maxResults=max_results)
        print(f"\n✓ Found {len(issues)} issue(s)")
        return issues
    except Exception as e:
        print(f"✗ Search failed: {e}")
        return []

def display_issues(issues):
    """Display issue information"""
    if not issues:
        print("No issues to display")
        return
    
    print("\n" + "="*80)
    for issue in issues:
        print(f"\nKey: {issue.key}")
        print(f"Summary: {issue.fields.summary}")
        print(f"Status: {issue.fields.status.name}")
        print(f"Priority: {getattr(issue.fields.priority, 'name', 'None') if issue.fields.priority else 'None'}")
        assignee = getattr(issue.fields.assignee, 'displayName', 'Unassigned') if issue.fields.assignee else 'Unassigned'
        print(f"Assignee: {assignee}")
        print("-"*80)

def main():
    """Main function"""
    print("Jira API Example Script")
    print("="*80)
    
    # Connect to Jira
    jira = connect_to_jira()
    if not jira:
        return
    
    # Example 1: Search for recently created issues
    print("\nExample 1: Recently created issues")
    issues = search_issues(jira, "created >= -7d ORDER BY created DESC", 5)
    display_issues(issues)
    
    # Example 2: Search for my open issues
    print("\n\nExample 2: My open issues")
    issues = search_issues(jira, "assignee = currentUser() AND resolution = Unresolved", 5)
    display_issues(issues)
    
    # Example 3: High priority issues
    print("\n\nExample 3: High priority issues")
    issues = search_issues(jira, "priority = High ORDER BY updated DESC", 5)
    display_issues(issues)
    
    print("\n" + "="*80)
    print("\nFor more JQL examples, see the README.md file")
    print("To use the GUI application, run: python jira_viewer.py")

if __name__ == "__main__":
    main()
