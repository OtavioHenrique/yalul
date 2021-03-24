from yalul.parsers.ast.nodes.statements.expressions.values.null import Null


class Environment:
    def __init__(self, variables_table):
        self.variables_table = variables_table

    def add_variable(self, identifier, value):
        self.variables_table[identifier] = value

    def get_variable(self, identifier):
        if self.variable_exists(identifier):
            return self.variables_table[identifier]
        else:
            return Null('null')

    def variable_exists(self, identifier):
        try:
            self.variables_table[identifier]
        except KeyError:
            return False
        else:
            return True

    def variables_table(self):
        return self.variables_table
