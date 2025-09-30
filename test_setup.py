#!/usr/bin/env python3
"""
Demo/Test script for Jira Viewer
This script validates the key components without requiring actual Jira credentials.
"""

import sys
import os

# Test 1: Import validation
print("=" * 60)
print("Test 1: Validating imports...")
print("=" * 60)

try:
    import tkinter as tk
    from tkinter import ttk, scrolledtext, messagebox
    print("✓ Tkinter imports successful")
except ImportError as e:
    print(f"✗ Tkinter import failed: {e}")
    sys.exit(1)

try:
    from dotenv import load_dotenv
    print("✓ python-dotenv import successful")
except ImportError as e:
    print(f"✗ python-dotenv import failed: {e}")
    sys.exit(1)

try:
    from jira import JIRA
    print("✓ jira library import successful")
except ImportError as e:
    print(f"✗ jira library import failed: {e}")
    sys.exit(1)

try:
    import webbrowser
    print("✓ webbrowser import successful")
except ImportError as e:
    print(f"✗ webbrowser import failed: {e}")
    sys.exit(1)

# Test 2: Module structure validation
print("\n" + "=" * 60)
print("Test 2: Validating module structure...")
print("=" * 60)

try:
    from jira_viewer import JiraViewer, main
    print("✓ JiraViewer class imported successfully")
    print("✓ main function imported successfully")
except ImportError as e:
    print(f"✗ Module import failed: {e}")
    sys.exit(1)

# Test 3: Class initialization validation (without GUI display)
print("\n" + "=" * 60)
print("Test 3: Validating class structure...")
print("=" * 60)

try:
    # Check if class has required methods
    required_methods = [
        'create_widgets',
        'connect_jira',
        'set_query',
        'search_issues',
        'clear_results',
        'show_issue_details',
        'open_in_browser',
        'copy_key'
    ]
    
    for method in required_methods:
        if hasattr(JiraViewer, method):
            print(f"✓ Method '{method}' exists")
        else:
            print(f"✗ Method '{method}' missing")
            sys.exit(1)
except Exception as e:
    print(f"✗ Class validation failed: {e}")
    sys.exit(1)

# Test 4: File structure validation
print("\n" + "=" * 60)
print("Test 4: Validating project files...")
print("=" * 60)

required_files = {
    'jira_viewer.py': 'Main application file',
    'requirements.txt': 'Python dependencies',
    '.env.example': 'Environment configuration template',
    '.gitignore': 'Git ignore rules',
    'README.md': 'Documentation'
}

for filename, description in required_files.items():
    filepath = f'/home/runner/work/jira/jira/{filename}'
    if os.path.exists(filepath):
        size = os.path.getsize(filepath)
        print(f"✓ {filename} exists ({size} bytes) - {description}")
    else:
        print(f"✗ {filename} missing - {description}")
        sys.exit(1)

# Test 5: Environment configuration validation
print("\n" + "=" * 60)
print("Test 5: Validating environment configuration...")
print("=" * 60)

with open('/home/runner/work/jira/jira/.env.example', 'r') as f:
    env_content = f.read()
    required_vars = ['JIRA_SERVER', 'JIRA_USERNAME', 'JIRA_API_TOKEN']
    for var in required_vars:
        if var in env_content:
            print(f"✓ {var} documented in .env.example")
        else:
            print(f"✗ {var} missing from .env.example")
            sys.exit(1)

# Summary
print("\n" + "=" * 60)
print("ALL TESTS PASSED! ✓")
print("=" * 60)
print("\nThe Jira Viewer application is properly configured.")
print("\nTo use the application:")
print("1. Copy .env.example to .env")
print("2. Fill in your Jira credentials in .env")
print("3. Run: python jira_viewer.py")
print("\nFor more information, see README.md")
