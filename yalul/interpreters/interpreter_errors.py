class InterpreterErrors:
    def __init__(self):
        self.errors = []

    def add(self, new_error):
        self.errors.append(new_error)
