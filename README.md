# click-app cookiecutter template

[![Tests](https://github.com/RKeelan/click-app/actions/workflows/test.yml/badge.svg)](https://github.com/RKeelan/click-app/actions/workflows/test.yml)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/RKeelan/click-app/blob/master/LICENSE)

Cookiecutter template for creating new [Click](https://click.palletsprojects.com/) command-line tools.

Use this template on your own machine with cookiecutter, or create a brand new repository based on this template entirely through the GitHub web interface using [click-app-template-repository](https://github.com/simonw/click-app-template-repository).


## Usage

Run `uvx cookiecutter gh:rkeelan/click-app` and then answer the prompts. Here's an example run:
```
$ cookiecutter gh:RKeelan/click-app
  [1/8] title (): Demo App
  [2/8] description (): Demonstration of https://github.com/rkeelan/click-app
  [3/8] app_name (DemoApp): 
  [4/8] package_name (demo-app): 
  [5/8] package_folder (demo_app): 
  [6/8] Select publish_to_pypi
    1 - y
    2 - n
  [7/8] github_username (RKeelan): 
  [8/8] author_name (R. Keelan):
```
The values in parentheses are defaults, which you can select by hitting enter. This will create a directory called `DemoApp` (the application name is the title converted to upper camel case).

The default `README.md` explains how to begin developping the application

## Create a Git repository and push it to GitHub

You can initialize a Git repository for your tool like this:
```powershell
$app = "DemoApp"
cd $app
$owner = "RKeelan"
$description = (Get-Content -Path "pyproject.toml" | Where-Object { $_ -match "description\s*=\s*(.*)" } | ForEach-Object { $matches[1] }).Trim('"''')

git init
git add .
git commit -m "Initial structure from template"
git branch -m master main

gh repo create "$owner/$app" --source . --description $description --public --push
```
The template will have created a GitHub Action which runs your tool's test suite against every commit.
