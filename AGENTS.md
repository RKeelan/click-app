# AGENTS.md

Read `README.md` first for template usage and the standard development workflow.

## Repository Guidance

- The cookiecutter template lives under `{{cookiecutter.app_name}}/`; changes there should keep the generated project coherent as a whole.
- Keep `cookiecutter.json`, the generated project files, and the README examples aligned when you add or rename template variables.
- The generated applications are Click-based Python CLIs; preserve the expected entry-point pattern in `{{cookiecutter.package_folder}}/cli.py` and `__main__.py`.
- Run `python -m pytest` before handing work off.
