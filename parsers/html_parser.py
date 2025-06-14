from bs4 import BeautifulSoup

# Function to parse HTML file
def parse_html(file_path):
    with open(file_path, 'r') as file:
        soup = BeautifulSoup(file, 'html.parser')
    return soup
