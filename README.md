# 3DBAG documentation

## Contributing

The documentation is made with [MkDocs](https://www.mkdocs.org/), read its documentation for the details.

1) Clone the repo

2) Install python packages:

    `pip install mkdocs mkdocs-material`

3) Edit the pages in `docs/`

4) If you edited the attribute catalogue, generate the attribute pages

   `python scripts/generate_attribute_doc.py . 'en'`

5) Build the pages locally
   
   `bash scripts/build.sh`

6) View the generated files
   
   `python -m http.server 8000 --directory generated`

### Theme

The documentation uses the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme, read its documentation for the details.

### Project layout

The multi-language project layout follows the proposal as described in [https://github.com/squidfunk/mkdocs-material/discussions/2346](https://github.com/squidfunk/mkdocs-material/discussions/2346).

```
    config/                # MkDocs project configuration files per language
         en/
            mkdocs.yml
         nl/
            mkdocs.yml
    docs/                  # Documentation content per language. Language-specific figures also go here.
         en/
            index.md
            ...
         nl/
            index.md
            ...
   images_common           # Contains the images that are common to both languages
   scripts/                # Utility scripts
   overrides/              # Template overrides, e.g. favicon, logo
```


### Documenting the data attributes

The attribute catalogue is a `.json` file in `docs/attributes.json`. The attribute documentation that is displayed in the website is auto-generated from the attribute catalogue, thus the attribute markdown files are completely overwritten. **Do not edit directly the attribute markdown files!**.

The attribute pages are generated with the `generate_attribute_doc.py` script.

`python scripts/generate_attribute_doc.py <project root dir> <language id>`

The attribute catalogue follows a specified schema. Each attribute in the catalogue must have an English (`en`) and Dutch (`nl`) description.

```json
  "<attribute name>": {
    "<language ID ('en' | 'nl')>": {
      "description": "<Attribute description. Mind the period at the end of the sentence.>.",
      "type": "<data type ( cardinal number | nominal number | real number | categorical | text | list ) >",
      "unit": "<unit of measurement>",
      "<optional, only for categorcial> values": {
        "<categorical value>": "<Value description. Mind the period at the end of the sentence.>."
      }
    }
  }
```

### Documenting data layers

Works the same way as the attributes, but with a different python script and json catalogue.

## 3DBAG organisation

This software is part of the 3DBAG project. For more information visit the [3DBAG organisation](https://github.com/3DBAG).
