PYTHON_FILE_PATHS = `(find . -iname "*.py" -not -path "./.venv/*")`

install: ## Install dependencies
	poetry install

pytest: ## Run tests
	poetry run pytest

hard-install: ## Delete .venv folder, and then install dependencies using poetry
	poetry env remove --all
	poetry install

