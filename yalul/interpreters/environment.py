from yalul.parsers.ast.nodes.statements.expressions.values.null import Null


class Environment:
    def __init__(self, environment_table):
        self.environment_table = environment_table

    def add_variable(self, identifier, value):
        self.environment_table[identifier] = value

    def get_variable(self, identifier):
        if self.variable_exists(identifier):
            return self.environment_table[identifier]
        else:
            return Null('null')

    def variable_exists(self, identifier):
        try:
            self.environment_table[identifier]
        except KeyError:
            return False
        else:
            return True

    def show_environment_table(self):
        return self.environment_table
