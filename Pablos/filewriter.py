class FileWriter:

    def __init__(self, filename) -> None:
        self.file = open(filename, "a")

    def write(self, text):
        self.file.write(text)
