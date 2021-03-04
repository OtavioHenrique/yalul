class ParseErrors:
    def __init__(self, errors):
        self.errors = errors

    def add_error(self, error):
        return self.errors.append(error)
