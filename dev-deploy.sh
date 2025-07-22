#!/usr/bin/env sh

# abort on errors
set -e

# build
make build

# navigate into the build output directory
cd generated

rsync -rzhP --delete --exclude=".*" . godzilla:/var/www/3dbag-docs-dev
ssh godzilla "chgrp staff3d -R /var/www/3dbag-docs-dev"

cd -
