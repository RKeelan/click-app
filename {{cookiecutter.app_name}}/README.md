# {{ cookiecutter.app_name }}

{% if cookiecutter.github_username %}[![Changelog](https://img.shields.io/github/v/release/{{ cookiecutter.github_username }}/{{ cookiecutter.app_name }}?include_prereleases&label=changelog)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.app_name }}/releases)
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

Install dependencies (including test):
```powershell
uv pip install -e '.[test]'
```

Run the tests:
```powershell
python -m pytest
```

Run the app:
```powershell
{{ cookiecutter.app_name }} --version
```
