import xml.etree.ElementTree as ElTree
import zipfile


def load_xml_data(file_path):
    """Load and parse XML data from a file or ZIP archive."""
    try:
        if file_path.endswith('.zip'):
            with zipfile.ZipFile(file_path, 'r') as z:
                # Assuming the XML file inside the ZIP has the same name as the ZIP without the .zip extension
                xml_file_name = "export_full.xml"
                with z.open(xml_file_name) as xml_file:
                    tree = ElTree.parse(xml_file)
        else:
            tree = ElTree.parse(file_path)

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
