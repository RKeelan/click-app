#!/usr/bin/env python3

import os
import tempfile
import subprocess
from pathlib import Path
import pytest
from cookiecutter.main import cookiecutter


def test_template_generation():
    """Test that the template generates successfully with default values"""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Generate the template
        result_dir = cookiecutter(
            template='.',
            output_dir=temp_dir,
            no_input=True,
            extra_context={'title': 'Test App'}
        )
        
        # Check that the project was created
        project_path = Path(result_dir)
        assert project_path.exists(), "Project directory should be created"
        
        # Check essential files exist
        assert (project_path / "pyproject.toml").exists(), "pyproject.toml should exist"
        assert (project_path / "README.md").exists(), "README.md should exist"
        assert (project_path / "LICENSE").exists(), "LICENSE should exist"
        
        # Check package structure
        package_dir = project_path / "test_app"
        assert package_dir.exists(), "Package directory should exist"
        assert (package_dir / "__init__.py").exists(), "__init__.py should exist"
        assert (package_dir / "cli.py").exists(), "cli.py should exist"
        assert (package_dir / "__main__.py").exists(), "__main__.py should exist"
        
        # Check tests directory
        tests_dir = project_path / "tests"
        assert tests_dir.exists(), "Tests directory should exist"
        assert (tests_dir / "test_test_app.py").exists(), "Test file should exist"


def test_generated_project_installs():
    """Test that the generated project can be installed"""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Generate the template
        result_dir = cookiecutter(
            template='.',
            output_dir=temp_dir,
            no_input=True,
            extra_context={'title': 'Test App'}
        )
        
        # Try to install the generated project
        result = subprocess.run(
            ['python', '-m', 'pip', 'install', '-e', '.'],
            cwd=result_dir,
            capture_output=True,
            text=True
        )
        
        assert result.returncode == 0, f"Installation failed: {result.stderr}"


def test_generated_project_tests_pass():
    """Test that the generated project's tests pass"""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Generate the template
        result_dir = cookiecutter(
            template='.',
            output_dir=temp_dir,
            no_input=True,
            extra_context={'title': 'Test App'}
        )
        
        # Install test dependencies
        subprocess.run(
            ['pip', 'install', '-e', '.[test]'],
            cwd=result_dir,
            check=True,
            capture_output=True
        )
        
        # Run the tests
        result = subprocess.run(
            ['python', '-m', 'pytest'],
            cwd=result_dir,
            capture_output=True,
            text=True
        )
        
        assert result.returncode == 0, f"Tests failed: {result.stdout}\n{result.stderr}"


def test_cli_works():
    """Test that the generated CLI application works"""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Generate the template
        result_dir = cookiecutter(
            template='.',
            output_dir=temp_dir,
            no_input=True,
            extra_context={'title': 'Test App'}
        )
        
        # Install the project
        subprocess.run(
            ['python', '-m', 'pip', 'install', '-e', '.'],
            cwd=result_dir,
            check=True,
            capture_output=True
        )
        
        # Test CLI version command
        result = subprocess.run(
            ['TestApp', '--version'],
            capture_output=True,
            text=True
        )
        
        assert result.returncode == 0, f"CLI failed: {result.stderr}"
        assert "version" in result.stdout.lower(), "Version should be in output"


@pytest.mark.parametrize("title,expected_package", [
    ("My Cool App", "my_cool_app"),
    ("Test123", "test123"),
    ("hyphen-app", "hyphen_app"),
])
def test_package_naming_conventions(title, expected_package):
    """Test that package names are generated correctly from titles"""
    with tempfile.TemporaryDirectory() as temp_dir:
        result_dir = cookiecutter(
            template='.',
            output_dir=temp_dir,
            no_input=True,
            extra_context={'title': title}
        )
        
        # Check that the package directory was created with correct name
        package_dir = Path(result_dir) / expected_package
        assert package_dir.exists(), f"Package directory {expected_package} should exist" 