class VarAssignmentInterpreter:
    """
    VarAssignmentInterpreter interprets all var assignment expressions
    """

    def __init__(self, identifier, value, env, error):
        self.identifier = identifier
        self.value = value
        self.env = env
        self.error = error

    def execute(self):
        """
        Interpret the expression
        """
        if self.env.variable_exists(self.identifier):
            self.env.add_variable(self.identifier, self.value)
            return self.value
        else:
            self.error.add(
                'Interpreter Error: Can\'t assign value {} to variable named "{}" because it doesn\'t exists'.format(
                    self.value, self.identifier))
