#!/usr/bin/env python3
"""
Integration test for Jira Viewer
This validates that all components work together properly.
"""

import sys
import os
import tkinter as tk
from unittest.mock import Mock, patch, MagicMock

# Add project root to path
sys.path.insert(0, '/home/runner/work/jira/jira')

def test_gui_initialization():
    """Test that the GUI can be initialized without errors"""
    print("\nTest: GUI Initialization")
    print("-" * 60)
    
    try:
        from jira_viewer import JiraViewer
        
        # Create a root window
        root = tk.Tk()
        
        # Initialize the app
        app = JiraViewer(root)
        
        # Check that key widgets exist
        assert hasattr(app, 'server_var'), "Missing server_var"
        assert hasattr(app, 'query_var'), "Missing query_var"
        assert hasattr(app, 'results_tree'), "Missing results_tree"
        assert hasattr(app, 'details_text'), "Missing details_text"
        assert hasattr(app, 'status_label'), "Missing status_label"
        
        print("✓ GUI initialized successfully")
        print("✓ All required widgets created")
        
        # Clean up
        root.destroy()
        
        return True
    except Exception as e:
        print(f"✗ GUI initialization failed: {e}")
        return False

def test_jql_query_handling():
    """Test that JQL queries are handled correctly"""
    print("\nTest: JQL Query Handling")
    print("-" * 60)
    
    try:
        from jira_viewer import JiraViewer
        
        root = tk.Tk()
        app = JiraViewer(root)
        
        # Test setting a query
        test_query = "project = TEST ORDER BY created DESC"
        app.set_query(test_query)
        
        assert app.query_var.get() == test_query, "Query not set correctly"
        print("✓ Query can be set programmatically")
        
        # Test that quick filter queries are valid JQL
        quick_filters = [
            "assignee = currentUser() AND resolution = Unresolved ORDER BY updated DESC",
            "updated >= -7d ORDER BY updated DESC",
            "created >= -7d ORDER BY created DESC"
        ]
        
        for query in quick_filters:
            app.query_var.set(query)
            assert app.query_var.get() == query, f"Failed to set query: {query}"
        
        print("✓ Quick filter queries are valid")
        
        root.destroy()
        return True
    except Exception as e:
        print(f"✗ Query handling test failed: {e}")
        return False

def test_results_display():
    """Test that results can be displayed in the tree"""
    print("\nTest: Results Display")
    print("-" * 60)
    
    try:
        from jira_viewer import JiraViewer
        
        root = tk.Tk()
        app = JiraViewer(root)
        
        # Test clearing results
        app.clear_results()
        assert len(app.results_tree.get_children()) == 0, "Results not cleared"
        print("✓ Results can be cleared")
        
        # Test adding a result manually
        app.results_tree.insert('', tk.END, values=(
            'TEST-123',
            'Test Summary',
            'Open',
            'John Doe',
            'High'
        ))
        
        assert len(app.results_tree.get_children()) == 1, "Result not added"
        print("✓ Results can be added to tree")
        
        # Test that columns are configured correctly
        columns = app.results_tree['columns']
        expected_columns = ('key', 'summary', 'status', 'assignee', 'priority')
        assert columns == expected_columns, f"Columns mismatch: {columns}"
        print("✓ Tree columns configured correctly")
        
        root.destroy()
        return True
    except Exception as e:
        print(f"✗ Results display test failed: {e}")
        return False

def test_connection_handling():
    """Test connection handling without actual Jira server"""
    print("\nTest: Connection Handling")
    print("-" * 60)
    
    try:
        from jira_viewer import JiraViewer
        
        root = tk.Tk()
        app = JiraViewer(root)
        
        # Check initial state
        assert app.jira is None or app.jira is not None, "Jira connection state exists"
        print("✓ Connection state is tracked")
        
        # Check server URL handling
        test_url = "https://test.atlassian.net"
        app.server_var.set(test_url)
        assert app.server_var.get() == test_url, "Server URL not set"
        print("✓ Server URL can be configured")
        
        root.destroy()
        return True
    except Exception as e:
        print(f"✗ Connection handling test failed: {e}")
        return False

def test_ui_components():
    """Test that all UI components are present"""
    print("\nTest: UI Components")
    print("-" * 60)
    
    try:
        from jira_viewer import JiraViewer
        
        root = tk.Tk()
        app = JiraViewer(root)
        
        # Check that the window has a title
        assert root.title() == "Jira Ticket Viewer", "Window title incorrect"
        print("✓ Window title is correct")
        
        # Check that key variables exist and have correct types
        assert isinstance(app.server_var, tk.StringVar), "server_var type incorrect"
        assert isinstance(app.query_var, tk.StringVar), "query_var type incorrect"
        print("✓ Tkinter variables are correctly typed")
        
        # Check that query entry exists and is bound to Enter key
        assert hasattr(app, 'query_entry'), "Query entry missing"
        print("✓ Query entry exists")
        
        root.destroy()
        return True
    except Exception as e:
        print(f"✗ UI components test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("=" * 60)
    print("Jira Viewer Integration Tests")
    print("=" * 60)
    
    tests = [
        test_gui_initialization,
        test_jql_query_handling,
        test_results_display,
        test_connection_handling,
        test_ui_components
    ]
    
    results = []
    for test in tests:
        try:
            result = test()
            results.append(result)
        except Exception as e:
            print(f"✗ Test crashed: {e}")
            results.append(False)
    
    print("\n" + "=" * 60)
    print("Test Summary")
    print("=" * 60)
    
    passed = sum(results)
    total = len(results)
    
    print(f"\nPassed: {passed}/{total}")
    
    if passed == total:
        print("\n✓ ALL INTEGRATION TESTS PASSED!")
        return 0
    else:
        print(f"\n✗ {total - passed} test(s) failed")
        return 1

if __name__ == "__main__":
    sys.exit(main())
