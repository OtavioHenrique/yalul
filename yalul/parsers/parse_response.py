class ParseResponse:
    def __init__(self, asts, errors):
        self.asts = asts
        self.errors = errors

    def show_errors(self):
        return self.errors.errors
