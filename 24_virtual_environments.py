# Virtual Environments in Python

print("=== Why Use Virtual Environments? ===")
print("""
Benefits:
- Isolated dependencies per project
- Avoid version conflicts
- Reproducible environments
- Clean global Python
""")

# 1. Creating Virtual Environment
print("\n=== Creating a Virtual Environment ===")
print("""
Commands:

python -m venv venv          # Create
# or
python3 -m venv venv

# Activate:
# Windows:    venv\\Scripts\\activate
# macOS/Linux: source venv/bin/activate

# Deactivate: deactivate
""")

# 2. Managing Dependencies
print("\n=== Managing Dependencies ===")
print("""
pip install numpy pandas requests
pip freeze > requirements.txt
pip install -r requirements.txt
""")

# 3. Check if running inside venv + List Installed Packages
print("\n=== Environment Information ===")

import sys

print(f"Python Executable : {sys.executable}")
print(f"Python Version    : {sys.version.split()[0]}")

in_venv = sys.prefix != sys.base_prefix
print(f"Running in Virtual Environment: {in_venv}")

# Modern way to list installed packages (replaces deprecated pkg_resources)
print("\n=== Installed Packages ===")
try:
    from importlib.metadata import distributions
    packages = [f"{dist.metadata['Name']}=={dist.version}" 
                for dist in distributions()]
    packages.sort()
    print("Total packages installed:", len(packages))
    print("First 10 packages:")
    for pkg in packages[:10]:
        print(pkg)
except Exception as e:
    print("Could not list packages:", e)

# 4. Best Practices
print("\n=== Best Practices ===")
print("""
1. One venv per project
2. Name folder 'venv' or '.venv'
3. Add venv/ to .gitignore
4. Always commit requirements.txt
5. Use requirements-dev.txt for development tools
""")

# 5. Alternative Tools
print("\n=== Alternative Tools ===")
print("""
• venv (built-in)
• conda (good for data science)
• poetry (modern dependency + packaging)
• pipenv
""")

print("\n=== Virtual Environments are essential for professional Python development! ===")