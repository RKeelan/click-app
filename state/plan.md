# Plan: Replace Cursor rules with CLAUDE.md and AGENTS.md

## Task 1: Replace Cursor rules with CLAUDE.md and AGENTS.md

### Requirements

- Remove the `.cursor/` directory from the template (`{{cookiecutter.app_name}}/.cursor/`)
- Create `{{cookiecutter.app_name}}/CLAUDE.md` that:
  - Uses `@include AGENTS.md` to include the agents file
  - Contains the same templated content currently in `repo.mdc` (description, architecture, CLI/API/UI, tasks sections), minus the Cursor-specific YAML front matter
- Create `{{cookiecutter.app_name}}/AGENTS.md` as a placeholder for agent-specific instructions (initially empty or with a minimal header)
- Update `{{cookiecutter.app_name}}/.gitignore`: remove the `.vscode` entry (unrelated to this change — skip if controversial)
- Update any tests that reference or assert the existence of `.cursor/` files

### Verification

- Run the existing test suite (`pytest`) and confirm all tests pass
- If tests assert the existence of `.cursor/rules/repo.mdc`, update them to assert `CLAUDE.md` and `AGENTS.md` instead

### Validation

- Generate a project from the template with `cookiecutter .` and verify:
  - No `.cursor/` directory exists in the output
  - `CLAUDE.md` exists and contains the `@include AGENTS.md` directive
  - `AGENTS.md` exists
  - The templated description appears correctly in `CLAUDE.md`
