from yalul.interpreters.expression_interpreter import ExpressionInterpreter


class VariableDeclarationInterpreter:
    """
    VariableDeclarationInterpreter interprets all variable declaration
    """

    def __init__(self, variable_declaration, environment, error):
        self.variable_declaration = variable_declaration
        self.environment = environment
        self.error = error

    def execute(self):
        """
        Interpret given statement
        """
        variable_value = ExpressionInterpreter.execute(self.variable_declaration.initializer,
                                                       self.environment, self.error)

        self.environment.add_variable(self.variable_declaration.name, variable_value)
