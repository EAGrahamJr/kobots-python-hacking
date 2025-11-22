# UV Quick Reference

## Common Commands

### Installing dependencies
```bash
uv sync                    # Install all dependencies from pyproject.toml
```

### Running scripts
```bash
uv run python script.py    # Run a Python script with dependencies
uv run script.py           # Also works if script has shebang
```

### Managing dependencies
```bash
uv add package-name        # Add a new dependency
uv remove package-name     # Remove a dependency
uv lock                    # Update the lock file
```

### Working with virtual environment
```bash
source .venv/bin/activate  # Activate the venv manually
deactivate                 # Deactivate the venv
```

### Other useful commands
```bash
uv pip list                # List installed packages
uv pip freeze              # Show installed packages with versions
uv tree                    # Show dependency tree
```

## Migration Notes

This project was converted from pip to uv:
- Dependencies are now managed in `pyproject.toml`
- Lock file (`uv.lock`) ensures reproducible installs
- Virtual environment is at `.venv/` instead of `venv/`
- Use `uv run` instead of activating venv for most tasks
