class ParseResponse:
    def __init__(self, asts, parse_errors):
        self.asts = asts
        self.parse_errors = parse_errors

    def errors(self):
        return self.parse_errors.errors
