# DemoApp

[![Changelog](https://img.shields.io/github/v/release/RKeelan/DemoApp?include_prereleases&label=changelog)](https://github.com/RKeelan/DemoApp/releases)
[![Tests](https://github.com/RKeelan/DemoApp/actions/workflows/test.yml/badge.svg)](https://github.com/RKeelan/DemoApp/actions/workflows/test.yml)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/RKeelan/DemoApp/blob/master/LICENSE)



## Setup

Checkout the code:
```powershell
git clone https://github.com/RKeelan/DemoApp.git
cd DemoApp
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
demo-app -v
```
