# {{ cookiecutter.app_name }}

{% if cookiecutter.publish_to_pypi == "y" %}[![PyPI](https://img.shields.io/pypi/v/{{ cookiecutter.package_name }}.svg)](https://pypi.org/project/{{ cookiecutter.package_name }}/)
{% endif %}{% if cookiecutter.github_username %}[![Changelog](https://img.shields.io/github/v/release/{{ cookiecutter.github_username }}/{{ cookiecutter.app_name }}?include_prereleases&label=changelog)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.app_name }}/releases)
[![Tests](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.app_name }}/actions/workflows/test.yml/badge.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.app_name }}/actions/workflows/test.yml)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.app_name }}/blob/master/LICENSE){% endif %}

{{ cookiecutter.description }}

## Setup

Checkout the code:
```powershell
git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.app_name }}.git
cd {{ cookiecutter.app_name }}
```

Create a new virtual environment:
```powershell
uv venv && .venv\Scripts\activate.ps1
```

Install dependencies:
```powershell
uv sync
```

Run the app:
```powershell
{{ cookiecutter.app_name }} --version
```

## Development

Install test and dev dependcies:
```powershell
uv sync --all-extras
```

Install pre-commit hooks:
```powershell
pre-commit install
```

Format code and fix linting issues:
```powershell
ruff format . && ruff check --fix .
```

Run the tests:
```powershell
python -m pytest
```

Run tests with coverage:
```powershell
python -m pytest --cov={{ cookiecutter.package_folder }}
```