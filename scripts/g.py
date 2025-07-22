import argparse
from pathlib import Path
from tabulate import tabulate
from bag3d.specs.core import load_attributes_spec

parser = argparse.ArgumentParser(
    description="Generate Markdown documentation from the 3DBAG attribute specifications for the provided language."
)
parser.add_argument('--lang', choices=['en', 'nl'], required=True,
                    help='Language: en or nl')


def main():
    args = parser.parse_args()
    project_dir = Path(__file__).parent.parent.resolve()
    attributes_md = project_dir / "docs" / args.lang / "schema" / "attributes.md"
    specs = load_attributes_spec()

    with open(attributes_md, "w") as fo:

        newline_double = "\n\n"
        fo.write("# Data Attributes")
        fo.write(newline_double)
        fo.write(
            "Attributes specification file and schema: [https://downloads.3dbag.nl](https://downloads.3dbag.nl)")
        fo.write(newline_double)

        table_main_headers = ["Property", "Value"]
        table_values_headers = ["Attribute Value", "Description"]
        table_formats_headers = ["Data Format", "Property", "Value"]

        for attribute_name, attribute in specs.items():

            tablefmt = "github"


            table_main_content = []
            table_main_content.append(["Description", attribute.description.en])
            table_main_content.append(["Source", attribute.source])
            table_main_content.append(["Data Type", str(attribute.type)])
            table_main_content.append(["Unit", attribute.unit.en if attribute.unit else "-"])
            table_main_content.append(["Scale", attribute.scale.en if attribute.scale else "-"])
            table_main_content.append(["Precision", attribute.precision if attribute.precision else "-"])
            table_main_content.append(["Value Format", f"`{attribute.value_format}`" if attribute.value_format else "`-`"])
            table_main_content.append(["Nullable", attribute.nullable if attribute.nullable else "-"])
            table_main_content.append(["Semantic Type", attribute.semantic_type])
            table_str = tabulate(table_main_content, headers=table_main_headers, tablefmt=tablefmt)

            table_values_str = None
            if values := attribute.values:
                table_values_content = []
                for value, value_desc in values.items():
                    table_values_content.append([f"`{value}`", value_desc.en])
                table_values_str = tabulate(table_values_content, headers=table_values_headers, tablefmt=tablefmt)

            table_formats_str = None
            if cityjson := attribute.applies_to.cityjson:
                table_formats_content = []
                data_format = "CityJSON"
                for property, value in cityjson.items():
                    value_formatted = ", ".join(map(str, value)) if isinstance(value, list) else str(value)
                    table_formats_content.append([data_format, property.capitalize(), value_formatted])
                    table_formats_content.append([data_format, "Data Type", attribute.type.as_json()])
                if gpkg := attribute.applies_to.gpkg:
                    for property, value in gpkg.items():
                        data_format = "GeoPackage"
                        value_formatted = ", ".join(map(str, value)) if isinstance(value, list) else str(value)
                        table_formats_content.append([data_format, property.capitalize(), value_formatted])
                        table_formats_content.append([data_format, "Data Type", attribute.type.as_gpkg()])
                table_formats_str = tabulate(table_formats_content, headers=table_formats_headers, tablefmt=tablefmt)


            fo.write(f"## `{attribute_name}`")
            fo.write(newline_double)
            fo.write(table_str)
            fo.write(newline_double)
            if table_values_str:
                fo.write("**Attribute Values**")
                fo.write(newline_double)
                fo.write(table_values_str)
                fo.write(newline_double)
            if table_formats_str:
                fo.write("**Data Format Specifications**")
                fo.write(newline_double)
                fo.write(table_formats_str)
                fo.write(newline_double)


if __name__ == '__main__':
    main()
