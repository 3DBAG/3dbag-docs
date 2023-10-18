#!/usr/bin/env sh

# abort on errors
set -e

# build
source venv/bin/activate
python scripts/generate_attribute_doc.py . 'nl'
python scripts/generate_attribute_doc.py . 'en'
python scripts/generate_layers_docs.py . 'nl'
python scripts/generate_layers_docs.py . 'en'
bash scripts/build.sh

# navigate into the build output directory
cd generated

rsync -rzhP --delete --exclude=".*" . godzilla:/var/www/3dbag-docs-dev
ssh godzilla "chgrp staff3d -R /var/www/3dbag-docs-dev"

cd -
