import argparse
from pathlib import Path
from typing import Optional
from tabulate import tabulate
from bag3d.specs.core import load_attributes_spec, Attribute, DocumentationLanguage

# Constants
TABLE_FORMAT = "github"
DOUBLE_NEWLINE = "\n\n"


def format_value(value, verbatim: bool = False) -> str:
    """Format a value for display in markdown table."""
    if value is None:
        formatted = "-"
    elif isinstance(value, bool):
        formatted = str(value)
    elif isinstance(value, str) and value:
        formatted = value
    elif isinstance(value, list):
        formatted = ", ".join(map(str, value))
    else:
        formatted = str(value) if value else "-"
    if verbatim:
        formatted = f"`{formatted}`"
    return formatted


def create_main_table(attribute: Attribute, lang: DocumentationLanguage) -> str:
    """Create the main properties table for an attribute."""
    description = attribute.description.get_translation(lang)
    unit = attribute.unit.get_translation(lang) if attribute.unit else None
    scale = attribute.scale.get_translation(lang) if attribute.scale else None

    table_content = [
        ["Description", description],
        ["Source", format_value(attribute.source)],
        ["Data Type", format_value(attribute.type)],
        ["Unit", format_value(unit)],
        ["Scale", format_value(scale)],
        ["Precision", format_value(attribute.precision)],
        ["Value Format", format_value(attribute.value_format, verbatim=True)],
        ["Nullable", format_value(attribute.nullable)],
        ["Semantic Type", format_value(attribute.semantic_type)]
    ]

    if lang == DocumentationLanguage.EN:
        table_main_headers = ["Property", "Value"]
    else:
        table_main_headers = ["Eigenschap", "Waarde"]
    return tabulate(table_content, headers=table_main_headers, tablefmt=TABLE_FORMAT)


def create_values_table(attribute: Attribute, lang: DocumentationLanguage) -> Optional[
    str]:
    """Create the attribute values table if values exist."""
    if not attribute.values:
        return None

    table_content = []
    for value, value_desc in attribute.values.items():
        description = value_desc.get_translation(lang)
        table_content.append([format_value(value, verbatim=True), description])

    if lang == DocumentationLanguage.EN:
        table_values_headers = ["Attribute Value", "Description"]
    else:
        table_values_headers = ["Attribuutwaarde", "Omschrijving"]
    return tabulate(table_content, headers=table_values_headers, tablefmt=TABLE_FORMAT)


def create_formats_table(attribute: Attribute, lang: DocumentationLanguage) -> Optional[
    str]:
    """Create the data format specifications table."""
    table_content = []

    # Add CityJSON format info
    if cityjson := attribute.applies_to.cityjson:
        data_format = "CityJSON"
        for property_name, value in cityjson.items():
            table_content.append(
                [data_format, property_name.capitalize(), format_value(value)])
        table_content.append([data_format, "Data Type", attribute.type.as_json()])

    # Add GeoPackage format info
    if gpkg := attribute.applies_to.gpkg:
        data_format = "GeoPackage"
        for property_name, value in gpkg.items():
            table_content.append(
                [data_format, property_name.capitalize(), format_value(value)])
        table_content.append([data_format, "Data Type", attribute.type.as_gpkg()])

    if not table_content:
        return None

    if lang == DocumentationLanguage.EN:
        TABLE_FORMATS_HEADERS = ["Data Format", "Property", "Value"]
    else:
        TABLE_FORMATS_HEADERS = ["Bestandsformaat", "Eigenschap", "Waarde"]
    return tabulate(table_content, headers=TABLE_FORMATS_HEADERS, tablefmt=TABLE_FORMAT)


def attribute_to_markdown(attribute_name: str, attribute: Attribute,
                          lang: DocumentationLanguage) -> str:
    """Convert a single attribute to markdown documentation."""
    sections = []

    # Add attribute name as header
    sections.append(f"## `{attribute_name}`")

    # Add main properties table
    sections.append(create_main_table(attribute, lang))

    # Add values table if applicable
    if values_table := create_values_table(attribute, lang):
        table_title = "Attribute Values" if lang == DocumentationLanguage.EN else "Attribuutwaarden"
        sections.append(f"**{table_title}**")
        sections.append(values_table)

    # Add formats table if applicable
    if formats_table := create_formats_table(attribute, lang):
        table_title = "Dataformat availability" if lang == DocumentationLanguage.EN else "Beschikbaarheid bestandsformaten"
        sections.append(f"**{table_title}**")
        sections.append(formats_table)

    # Join all sections with double newlines
    return DOUBLE_NEWLINE.join(sections)


def write_header(lang: DocumentationLanguage) -> str:
    """Generate the document header."""
    if lang == DocumentationLanguage.EN:
        title = "Data Attributes"
        schema_text = "This is a list of all 3DBAG attributes"
    else:
        title = "Data Attributen"
        schema_text = "Dit is een lijst van alle 3DBAG attributen"
    return (
            f"# {title}" + DOUBLE_NEWLINE +
            f"{schema_text}."
    )


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Generate Markdown documentation from the 3DBAG attribute specifications for the provided language."
    )
    parser.add_argument('--lang', required=True,
                        type=DocumentationLanguage.from_string,
                        help='Language: en or nl')
    parser.add_argument('--root', required=True,
                        help='Project root directory')
    return parser.parse_args()


def main():
    args = parse_arguments()

    # Setup paths
    project_dir = Path(args.root).resolve()
    attributes_md = project_dir / "docs" / str(args.lang) / "schema" / "attributes.md"

    # Load specifications
    specs = load_attributes_spec()

    # Generate markdown
    with open(attributes_md, "w") as fo:
        # Write header
        fo.write(write_header(args.lang))
        fo.write(DOUBLE_NEWLINE)

        # Write each attribute
        for attribute_name, attribute in specs.items():
            fo.write(attribute_to_markdown(attribute_name, attribute, args.lang))
            fo.write(DOUBLE_NEWLINE)


if __name__ == '__main__':
    main()
