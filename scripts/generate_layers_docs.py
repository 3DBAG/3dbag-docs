import json
from pathlib import Path
import sys

project_dir = Path(sys.argv[1]).resolve()
lang = sys.argv[2]
# project_dir = Path("/home/balazs/Development/3dbag-docs").resolve()
# lang = "en"
assert lang in ("en", "nl")
layer_catalogue = project_dir / "docs" / "layers.json"
assert layer_catalogue.exists()
layers_md = project_dir / "docs" / lang / "schema" / "layers.md"

with Path(layer_catalogue).resolve().open("r") as fo:
    layers = json.load(fo)

layers_md_txt = layers_md.read_text()
marker_start = "<!-- start layers (DO NOT REMOVE THIS MARKER AND DO NOT EDIT THE TEXT BELOW. SEE README.) -->"
marker_end = "<!-- end layers (DO NOT REMOVE THIS MARKER) -->"
idx_start = layers_md_txt.find(marker_start) + len(marker_start)
idx_end = layers_md_txt.find(marker_end)

with layers_md.open("w") as fo:
    fo.write(layers_md_txt[:idx_start])

    for lname, ldesc in layers.items():
        if lang in ldesc:
            fo.write(f"\n## `{lname}`\n\n")
            fo.write(f"{ldesc[lang]['description']}\n\n")

    fo.write(layers_md_txt[idx_end:])
