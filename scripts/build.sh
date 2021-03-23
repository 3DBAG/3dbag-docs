mkdocs build -f config/en/mkdocs.yml
mkdocs build -f config/nl/mkdocs.yml
rm -rf generated/images_common
mkdir generated/images_common
cp images_common/* generated/images_common/