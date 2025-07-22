.PHONY: help venv install clean build serve_en serve_nl deploy-dev

# Variables
VENV_DIR = .venv
PYTHON = python3
PIP = $(VENV_DIR)/bin/pip
PYTHON_VENV = $(VENV_DIR)/bin/python

help: ## Show this help message
	@echo "Available targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

venv: ## Create virtual environment
	$(PYTHON) -m venv $(VENV_DIR)
	$(PIP) install --upgrade pip

install: ## Install the dependencies
	$(PIP) install -r requirements.txt

clean: ## Clean generated files
	rm -rf generated

build: ## Build documentation
	$(PYTHON_VENV) scripts/generate_layers_docs.py . "nl"
	$(PYTHON_VENV) scripts/generate_layers_docs.py . "en"
	$(PYTHON_VENV) scripts/generate_attribute_doc.py . "nl"
	$(PYTHON_VENV) scripts/generate_attribute_doc.py . "en"
	bash scripts/build.sh
	mkdir -p generated
	cp includes/CNAME generated/ 2>/dev/null || true
	cp includes/index.html generated/ 2>/dev/null || true

serve_en: ## Serve documentation locally
	$(VENV_DIR)/bin/mkdocs serve -f config/en/mkdocs.yml

serve_nl: ## Serve documentation locally
	$(VENV_DIR)/bin/mkdocs serve -f config/nl/mkdocs.yml

deploy-dev: build ## Build and prepare for deployment
	@echo "Documentation built in ./generated directory"
	@echo "Ready for deployment to gh-pages"