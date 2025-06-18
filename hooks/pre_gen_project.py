#!/usr/bin/env python
import re
import sys

# Validate project slug
MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'
project_slug = '{{ cookiecutter.project_slug }}'
package_name = '{{ cookiecutter.package_name }}'

if not re.match(MODULE_REGEX, package_name):
    print(f'ERROR: {package_name} is not a valid Python module name!')
    sys.exit(1)

print(f"✅ Creating MCP project: {project_slug}")
print(f"✅ Package name: {package_name}")
print("✅ All validations passed!")