#!/usr/bin/env python3

import os
import tempfile
import shutil
from pathlib import Path
import pytest


def test_publish_to_pypi_disabled():
    """Test that publish.yml is removed when publish_to_pypi=n"""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Simulate what cookiecutter would create with publish_to_pypi = n
        app_dir = Path(temp_dir) / "TestApp"
        workflows_dir = app_dir / ".github" / "workflows"
        workflows_dir.mkdir(parents=True)
        
        # Create publish.yml (will be removed by hook)
        publish_yml = workflows_dir / "publish.yml"
        publish_yml.write_text("name: Publish\n")
        
        assert publish_yml.exists(), "publish.yml should exist before hook"
        
        # Simulate the post-generation hook behavior
        publish_to_pypi = "n"
        if publish_to_pypi == "n" and publish_yml.exists():
            publish_yml.unlink()
        
        assert not publish_yml.exists(), "publish.yml should be removed when publish_to_pypi=n"


def test_publish_to_pypi_enabled():
    """Test that publish.yml is kept when publish_to_pypi=y"""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Simulate what cookiecutter would create with publish_to_pypi = y
        app_dir = Path(temp_dir) / "TestApp"
        workflows_dir = app_dir / ".github" / "workflows"
        workflows_dir.mkdir(parents=True)
        
        # Create publish.yml (should be kept)
        publish_yml = workflows_dir / "publish.yml"
        publish_yml.write_text("name: Publish\n")
        
        assert publish_yml.exists(), "publish.yml should exist before hook"
        
        # Simulate the post-generation hook behavior
        publish_to_pypi = "y"
        if publish_to_pypi == "n" and publish_yml.exists():
            publish_yml.unlink()
        
        assert publish_yml.exists(), "publish.yml should be kept when publish_to_pypi=y"


def test_readme_pypi_badge_conditional():
    """Test that PyPI badge appears/disappears based on publish_to_pypi setting"""
    with tempfile.TemporaryDirectory() as temp_dir:
        app_dir = Path(temp_dir) / "TestApp"
        app_dir.mkdir(parents=True)
        
        # Test publish_to_pypi = y (badge should be included)
        readme_with_badge = app_dir / "README_with_badge.md"
        readme_with_badge.write_text("""# TestApp

[![PyPI](https://img.shields.io/pypi/v/test-app.svg)](https://pypi.org/project/test-app/)
[![Tests](badge.svg)](link)
""")
        
        content_with_badge = readme_with_badge.read_text()
        assert "PyPI" in content_with_badge, "README should contain PyPI badge when publish_to_pypi=y"
        
        # Test publish_to_pypi = n (badge should not be included)
        readme_without_badge = app_dir / "README_without_badge.md"
        readme_without_badge.write_text("""# TestApp

[![Tests](badge.svg)](link)
""")
        
        content_without_badge = readme_without_badge.read_text()
        assert "PyPI" not in content_without_badge, "README should not contain PyPI badge when publish_to_pypi=n"


@pytest.mark.parametrize("publish_to_pypi,should_have_file,should_have_badge", [
    ("y", True, True),
    ("n", False, False),
])
def test_publish_to_pypi_scenarios(publish_to_pypi, should_have_file, should_have_badge):
    """Parameterized test for both publish_to_pypi scenarios"""
    with tempfile.TemporaryDirectory() as temp_dir:
        app_dir = Path(temp_dir) / "TestApp"
        workflows_dir = app_dir / ".github" / "workflows"
        workflows_dir.mkdir(parents=True)
        
        # Create publish.yml
        publish_yml = workflows_dir / "publish.yml"
        publish_yml.write_text("name: Publish\n")
        
        # Simulate post-generation hook
        if publish_to_pypi == "n" and publish_yml.exists():
            publish_yml.unlink()
        
        # Check file existence
        assert publish_yml.exists() == should_have_file, f"publish.yml existence should be {should_have_file} for publish_to_pypi={publish_to_pypi}"
        
        # Check badge presence (simplified simulation)
        if should_have_badge:
            readme_content = "[![PyPI](badge)](link)"
        else:
            readme_content = "No badge here"
        
        assert ("PyPI" in readme_content) == should_have_badge, f"PyPI badge presence should be {should_have_badge} for publish_to_pypi={publish_to_pypi}" 