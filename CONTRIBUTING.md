# Contributing to Jira Viewer

Thank you for your interest in contributing to Jira Viewer! This document provides guidelines for contributing to the project.

## Getting Started

1. Fork the repository
2. Clone your fork locally
3. Install dependencies: `pip install -r requirements.txt`
4. Create a branch for your changes: `git checkout -b feature/your-feature-name`

## Development Setup

1. Copy `.env.example` to `.env` and configure your Jira credentials
2. Run the setup test: `python test_setup.py`
3. Test the application: `python jira_viewer.py`

## Making Changes

### Code Style

- Follow PEP 8 Python style guidelines
- Use meaningful variable and function names
- Add comments for complex logic
- Keep functions focused and small

### Testing

Before submitting a pull request:

1. Run the setup validation:
```bash
python test_setup.py
```

2. Test your changes manually with the GUI:
```bash
python jira_viewer.py
```

3. Verify the example script still works:
```bash
python example_usage.py
```

### Commit Messages

- Use clear, descriptive commit messages
- Start with a verb (Add, Fix, Update, Remove, etc.)
- Keep the first line under 72 characters
- Add details in the commit body if needed

Example:
```
Add support for custom fields in issue details

- Parse custom fields from Jira API response
- Display custom fields in the details panel
- Update documentation with custom field examples
```

## Types of Contributions

We welcome:

- **Bug fixes**: Fix issues or incorrect behavior
- **Features**: Add new functionality
- **Documentation**: Improve or add documentation
- **Examples**: Add helpful examples or tutorials
- **UI/UX**: Improve the user interface
- **Performance**: Optimize code performance
- **Tests**: Add or improve tests

## Pull Request Process

1. Update documentation if you're changing functionality
2. Test your changes thoroughly
3. Submit a pull request with a clear description
4. Reference any related issues in your PR description
5. Be responsive to feedback and questions

## Questions or Problems?

- Open an issue for bugs or feature requests
- Use discussions for questions and general topics

## Code of Conduct

- Be respectful and inclusive
- Welcome newcomers
- Focus on constructive feedback
- Help others learn and grow

Thank you for contributing to Jira Viewer! 🎉
