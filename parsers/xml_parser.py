import xml.etree.ElementTree as ET

# Function to parse XML file
def parse_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    return root
