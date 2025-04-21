# click-app cookiecutter template

Cookiecutter template for creating new [Click](https://click.palletsprojects.com/) command-line tools.

Use this template on your own machine with cookiecutter, or create a brand new repository based on this template entirely through the GitHub web interface using [click-app-template-repository](https://github.com/simonw/click-app-template-repository).


## Usage

Run `uvx cookiecutter gh:rkeelan/click-app` and then answer the prompts. Here's an example run:
```
$ cookiecutter gh:RKeelan/click-app
  [1/7] title (): Demo App
  [2/7] description (): Demonstration of https://github.com/rkeelan/click-app
  [3/7] app_name (DemoApp): 
  [4/7] package_name (demo-app): 
  [5/7] package_folder (demo_app): 
  [6/7] github_username (RKeelan): 
  [7/7] author_name (R. Keelan):
```
The values in parentheses are defaults, which you can select by hitting enter. This will create a directory called `DemoApp` (the application name is the title converted to upper camel case).

The default `README.md` explains how to begin developping the application

## Create a Git repository and push it to GitHub

You can initialize a Git repository for your tool like this:
```powershell
$app = "DemoApp"
cd $app
$user = "RKeelan"
$description = (Get-Content -Path "pyproject.toml" | Where-Object { $_ -match "description\s*=\s*(.*)" } | ForEach-Object { $matches[1] }).Trim('"''')
git init
git add .
git commit -m "Initial structure from template"
git branch -m master main

gh auth login
gh repo create $app --source . --description $description --public --push
git remote add origin "https://github.com/$user/$app.git"
git push -u origin main
```
The template will have created a GitHub Action which runs your tool's test suite against every commit.
