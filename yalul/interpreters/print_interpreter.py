from yalul.interpreters.expression_interpreter import ExpressionInterpreter


class PrintInterpreter:
    """
    PrintInterpreter interprets all print statements
    """

    def __init__(self, print_statement, environment, error):
        self.print_statement = print_statement
        self.environment = environment
        self.error = error

    def execute(self):
        """
        Interpret given statement
        """
        value = ExpressionInterpreter.execute(self.print_statement.value,
                                              self.environment, self.error)

        print(value)
