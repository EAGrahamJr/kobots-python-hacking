.PHONY:
format:
	uv run ruff format pybot edlib *.py

.PHONY:
lint:
	uv run ruff lint pybot edlib *.py
