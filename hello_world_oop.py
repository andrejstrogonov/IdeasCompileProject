class HelloWorld:
    def __init__(self, file_path):
        self._file_path = file_path

    def _read_file(self):
        with open(self._file_path, 'r') as file:
            return file.readlines()

    def display(self):
        lines = self._read_file()
        for line in lines:
            print(line, end='')

if __name__ == "__main__":
    hello_world = HelloWorld('data/hello_world.txt')
    hello_world.display()
