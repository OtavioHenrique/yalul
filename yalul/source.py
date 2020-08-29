class Source:
    def __init__(self, file):
        self.file = file

    def read(self):
        return self.file.read()
