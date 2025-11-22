# Python Hack Scripts
Just random stuff used to explore things

## `brainz` and `marvin`

Interactive "environments" to play with :poop:. Run `py -i whichever.py`.


## Setup

This project uses [uv](https://docs.astral.sh/uv/) for fast, reliable Python package management.

### Installation

1. Install uv (if not already installed):
   ```bash
   pip install uv
   ```

2. Sync dependencies:
   ```bash
   uv sync
   ```

### Usage

Run scripts with uv:
```bash
uv run python script_name.py
```

Or activate the virtual environment:
```bash
source .venv/bin/activate
python script_name.py
```

### Adding Dependencies

Add new dependencies to `pyproject.toml` under `dependencies`, then run:
```bash
uv sync
```

Or install directly:
```bash
uv add package-name
```
