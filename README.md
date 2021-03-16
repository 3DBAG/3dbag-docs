# 3D BAG documentation

## Contributing

The documentation is made with [MkDocs](https://www.mkdocs.org/), read its documentation for the details.

1) Clone the repo

2) Install python packages:

    `pip install mkdocs mkdocs-material`

3) Edit the pages in `docs/`

4) Build the pages locally
   
   `build.sh`

5) View the generated files
   
   `python -m http.server 8000 --directory generated`

### Theme

The documentation uses the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme, read its documentation for the details.

### Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.

### Commands

+ `mkdocs serve` - Start the live-reloading docs server.
+ `mkdocs build` - Build the documentation site.
+ `mkdocs -h` - Print help message and exit.
