import sys

class HelloWorldParser:
    def __init__(self, file_path):
        self.file_path = file_path

    def parse_and_print(self):
        with open(self.file_path, 'r') as file:
            for line in file:
                sys.stdout.write(line)

if __name__ == "__main__":
    parser = HelloWorldParser('data/hello_world.txt')
    # Using reflection to call the method
    method_name = 'parse_and_print'
    method = getattr(parser, method_name)
    method()
