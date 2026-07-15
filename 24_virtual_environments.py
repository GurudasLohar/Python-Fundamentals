# Virtual Environments in Python

# Virtual Environments (venvs) allow you to have isolated Python setups per project.
# This prevents version conflicts and keeps your global Python clean.

print("=== Why Use Virtual Environments? ===")
print("""
Benefits:
- Project-specific dependencies
- Different versions of same package across projects
- Reproducible environments
- Cleaner global Python installation
""")

# 1. Creating a Virtual Environment
print("\n=== Creating a Virtual Environment ===")
print("""
Commands:

# Using built-in venv module
python -m venv myenv          # Create environment
# or
python3 -m venv myenv

# On Windows:
myenv\\Scripts\\activate

# On macOS/Linux:
source myenv/bin/activate
""")

# 2. Activating & Deactivating
print("\n=== Activating & Deactivating ===")
print("""
After activation, your terminal prompt changes.
You can now pip install packages that only affect this project.

To deactivate:
deactivate
""")

# 3. Managing Dependencies
print("\n=== Managing Dependencies ===")
print("""
# Install packages
pip install requests numpy pandas

# Save dependencies
pip freeze > requirements.txt

# Install from requirements
pip install -r requirements.txt

# Upgrade pip itself
python -m pip install --upgrade pip
""")

# 4. Best Practices
print("\n=== Best Practices ===")
print("""
1. Create one venv per project
2. Name it 'venv' or '.venv' (commonly ignored in .gitignore)
3. Always activate before working on the project
4. Commit requirements.txt to version control
5. Never commit the venv folder itself
6. Use requirements.txt + requirements-dev.txt for development
""")

# 5. Alternative Tools
print("\n=== Alternative Tools ===")
print("""
- venv (built-in, recommended for beginners)
- virtualenv (more features)
- conda / miniconda (great for data science & heavy packages)
- poetry (modern dependency management + packaging)
- pipenv
""")

# 6. Practical Demonstration Code
print("\n=== Inside a Virtual Environment ===")

import sys
print(f"Python executable: {sys.executable}")
print(f"Python version   : {sys.version.split()[0]}")

# Check if running in venv
if hasattr(sys, 'prefix') and hasattr(sys, 'base_prefix'):
    in_venv = sys.prefix != sys.base_prefix
    print(f"Running inside virtual environment: {in_venv}")

# Example of listing installed packages
print("\nInstalled packages (via pip):")
try:
    import pkg_resources
    installed = [f"{pkg.project_name}=={pkg.version}" 
                for pkg in pkg_resources.working_set]
    print(installed[:10])  # Show first 10
except ImportError:
    print("pkg_resources not available")

print("\n=== Virtual Environments are essential for professional Python development! ===")
print("""
Tip: Add a .gitignore file with:
venv/
.env
__pycache__/
*.pyc
""")