class VariableInterpreter:
    """
    VariableInterpreter interprets all variable expressions
    """

    def __init__(self, identifier, env, error):
        self.identifier = identifier
        self.env = env
        self.error = error

    def execute(self):
        """
        Interpret the expression
        """
        if self.env.variable_exists(self.identifier):
            return self.env.get_variable(self.identifier)
        else:
            self.error.add(
                'Interpreter Error: Variable "{}" not initialized'.format(self.identifier))
