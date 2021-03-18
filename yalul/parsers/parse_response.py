class ParseResponse:
    def __init__(self, ast, parse_errors):
        self.ast = ast
        self.parse_errors = parse_errors

    def errors(self):
        return self.parse_errors.errors
