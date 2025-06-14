import json
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

# Function to parse JSON file
def parse_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Function to parse XML file
def parse_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    return root

# Function to parse HTML file
def parse_html(file_path):
    with open(file_path, 'r') as file:
        soup = BeautifulSoup(file, 'html.parser')
    return soup

# Example usage
if __name__ == "__main__":
    json_data = parse_json('../data/hello_world.json')
    print("JSON Data:", json_data)

    xml_data = parse_xml('../data/hello_world.xml')
    print("XML Data:", xml_data)

    html_data = parse_html('../data/hello_world.html')
    print("HTML Data:", html_data.prettify())
