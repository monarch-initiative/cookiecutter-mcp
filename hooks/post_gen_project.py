#!/usr/bin/env python
import os
import subprocess

# Initialize git repository
try:
    subprocess.run(["git", "init"], check=True)
    print("✅ Git repository initialized")
    
    # Create .gitignore file
    with open(".gitignore", "w") as f:
        f.write("""# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Unit test / coverage reports
htmlcov/
.tox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
.hypothesis/

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Editor settings
.idea/
.vscode/
*.swp
*.swo
""")
    print("✅ .gitignore file created")
    
except Exception as e:
    print(f"⚠️ Warning: Could not initialize git repository: {e}")

print("\n🎉 Your MCP project is ready!")
print(f"📂 Project path: {os.getcwd()}")
print("\nNext steps:")
print("1. Create a virtual environment")
print("2. Install the package: `uv pip install -e .`")
print("3. Run the CLI: `{{ cookiecutter.project_slug }}`")
print("4. Develop your MCP tools in the tools.py file")