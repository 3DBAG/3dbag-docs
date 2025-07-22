.PHONY: help venv install clean build serve_en serve_nl deploy-dev

setup: ## Install the dependencies
	uv sync

clean: ## Clean generated files
	rm -rf generated

build: ## Build documentation
	uv run scripts/generate_layers_docs.py . "nl"
	uv run scripts/generate_layers_docs.py . "en"
	uv run scripts/generate_attribute_doc.py --lang "nl" --root .
	uv run scripts/generate_attribute_doc.py --lang "en" --root .
	uv run mkdocs build -f config/en/mkdocs.yml
	uv run mkdocs build -f config/nl/mkdocs.yml
	rm -rf generated/images_common
	mkdir generated/images_common
	cp images_common/* generated/images_common/
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