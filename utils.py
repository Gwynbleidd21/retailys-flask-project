import xml.etree.ElementTree as ElTree


def load_xml_data(xml_file):
    """Load and parse XML data from a file."""
    try:
        tree = ElTree.parse(xml_file)
        root = tree.getroot()

        product_names = [item.get('name') for item in root.findall('.//item')]

        spare_parts_dict = {}
        for item in root.findall('.//item'):
            product_name = item.get('name')
            parts_section = item.find('parts')
            if parts_section is not None:
                parts = [part_item.get('name') for part_item in parts_section.findall('.//item')]
                if parts:
                    spare_parts_dict[product_name] = parts

        return product_names, spare_parts_dict

    except Exception as e:
        print(f"Error loading XML data: {e}")
        return [], {}
