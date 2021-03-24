import json
from pathlib import Path
import sys

project_dir = Path(sys.argv[1]).resolve()
lang = sys.argv[2]
# project_dir = Path("/home/balazs/Development/3dbag-docs").resolve()
# lang = "en"
assert lang in ("en", "nl")
attribute_catalogue = project_dir / "docs" / "attributes.json"
assert attribute_catalogue.exists()
attributes_md = project_dir / "docs" / lang / "schema" / "attributes.md"

with Path(attribute_catalogue).resolve().open("r") as fo:
    _a = json.load(fo)
    attr = {k: _a[k] for k in sorted(_a)}
    del _a

if lang == "en":
    type_txt = "*Data type*"
    unit_txt = "*Unit*"
    source_txt = "*Source*"
    values_txt = "*Values*"
    values_tbl_header = "| Values | Description |\n| :---- | :---------- |\n"
else:
    type_txt = "*Datatype*"
    unit_txt = "*Eenheid*"
    source_txt = "*Bron*"
    values_txt = "*Waarden*"
    values_tbl_header = "| Waarden | Omschrijving |\n| :----- | :----------- |\n"

with attributes_md.open("w") as fo:
    if lang == "en":
        fo.write("# Data Attributes\n\n")
    else:
        fo.write("# Data Attributen\n\n")

    for aname, adesc in attr.items():
        if lang in adesc:
            fo.write(f"\n## `{aname}`\n\n")
            fo.write(f"{adesc[lang]['description']}\n\n")
            fo.write(f"{type_txt}: {adesc[lang]['type']}\n\n")
            fo.write(f"{unit_txt}: {adesc[lang]['unit']}\n\n")
            if "source" in adesc[lang]:
                fo.write(f"{source_txt}: {adesc[lang]['source']}\n\n")
            if "values" in adesc[lang]:
                fo.write(f"{values_txt}:\n\n")
                fo.write(values_tbl_header)
                for k, v in adesc[lang]["values"].items():
                    fo.write(f"| `{k}` | {v} |\n")
