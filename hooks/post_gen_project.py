#!/usr/bin/env python3

import os
import shutil

def main():
    publish_to_pypi = "{{ cookiecutter.publish_to_pypi }}"
    
    if publish_to_pypi == "n":
        # Remove the publish workflow file if not publishing to PyPI
        publish_workflow = ".github/workflows/publish.yml"
        if os.path.exists(publish_workflow):
            os.remove(publish_workflow)
            print(f"Removed {publish_workflow} (publish_to_pypi=n)")

if __name__ == "__main__":
    main() 