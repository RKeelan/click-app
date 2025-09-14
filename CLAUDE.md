# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Cookiecutter template for creating Click-based command-line applications. The template generates a complete Python CLI project structure with:

- Click-based CLI framework
- Testing setup with pytest and coverage
- Code formatting/linting with Ruff
- Pre-commit hooks for code quality
- GitHub Actions CI/CD workflows
- Optional PyPI publishing configuration

## Template Structure

The main template is located in `{{cookiecutter.app_name}}/` directory, containing:
- `{{cookiecutter.package_folder}}/cli.py` - Main CLI entry point using Click
- `{{cookiecutter.package_folder}}/__main__.py` - Module execution entry point
- `tests/` - Test directory with pytest configuration
- `pyproject.toml` - Project configuration with dependencies and tool settings
- `.pre-commit-config.yaml` - Pre-commit hooks configuration
- `.github/workflows/` - GitHub Actions workflows for testing and publishing

## Development Commands

### Template Development (this repository)
```bash
# Run template tests
python -m pytest

# Test template generation
cookiecutter .

# Install template from GitHub
uvx cookiecutter gh:rkeelan/click-app
```

### Generated Project Commands (after using template)
```bash
# Setup virtual environment
uv venv && source .venv/bin/activate  # Linux/Mac
uv venv && .venv\Scripts\activate.ps1  # Windows PowerShell

# Install dependencies
uv sync

# Install with development dependencies
uv sync --all-extras

# Run the generated CLI application
<app_name> --version

# Development workflow
pre-commit install              # Install pre-commit hooks
ruff format . && ruff check --fix .  # Format and lint code
python -m pytest              # Run tests
python -m pytest --cov=<package_folder>  # Run tests with coverage
```

## Configuration Details

### Code Quality Tools
- **Ruff**: Used for both formatting and linting (replaces Black and flake8)
- **pytest**: Testing framework with coverage reporting (minimum 75% coverage required)
- **pre-commit**: Automated code quality checks before commits

### Template Variables
The cookiecutter.json defines template variables that get substituted throughout the template:
- `title` - Project display name
- `app_name` - Generated executable name (CamelCase from title)
- `package_name` - PyPI package name (kebab-case from title)
- `package_folder` - Python module name (snake_case from title)
- `publish_to_pypi` - Whether to include PyPI publishing workflow
- `github_username` - GitHub username for repository URLs
- `author_name` - Package author name

### GitHub Workflows
- **test.yml**: Runs tests on Python 3.10-3.12 for all pushes/PRs
- **publish.yml**: Publishes to PyPI on tag creation (if enabled)

## Architecture Notes

The generated CLI applications follow this pattern:
- Single entry point in `cli.py` with Click decorators
- Module can be executed with `python -m <package_name>` via `__main__.py`
- Console script registered in pyproject.toml for direct execution
- Minimal dependencies (only Click required for runtime)
- Development tools configured in optional dependencies groups

The template uses modern Python packaging standards with pyproject.toml instead of setup.py, and leverages uv for fast dependency management.