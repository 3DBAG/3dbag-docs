.PHONY: help venv install clean build serve_en serve_nl deploy-dev

setup: ## Install the dependencies
	uv sync

clean: ## Clean generated files
	rm -rf generated

build: ## Build documentation
	uv run scripts/generate_layers_docs.py . "nl"
	uv run scripts/generate_layers_docs.py . "en"
	uv run scripts/generate_attribute_doc.py . "nl"
	uv run scripts/generate_attribute_doc.py . "en"
	bash scripts/build.sh
	mkdir -p generated
	cp includes/CNAME generated/ 2>/dev/null || true
	cp includes/index.html generated/ 2>/dev/null || true

serve_en: ## Serve documentation locally
	uv run mkdocs serve -f config/en/mkdocs.yml

serve_nl: ## Serve documentation locally
	uv run mkdocs serve -f config/nl/mkdocs.yml

deploy-dev: build ## Build and prepare for deployment
	@echo "Documentation built in ./generated directory"
	@echo "Ready for deployment to gh-pages"