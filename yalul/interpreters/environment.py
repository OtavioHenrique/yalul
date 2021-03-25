from yalul.parsers.ast.nodes.statements.expressions.values.null import Null


class Environment:
    def __init__(self, variables_table, func_table):
        self.__variables_table = variables_table
        self.__func_table = func_table

    def add_variable(self, identifier, value):
        self.__variables_table[identifier] = value

    def get_variable(self, identifier):
        if self.variable_exists(identifier):
            return self.__variables_table[identifier]
        else:
            return Null('null')

    def variable_exists(self, identifier):
        try:
            self.__variables_table[identifier]
        except KeyError:
            return False
        else:
            return True

    def variables_table(self):
        return self.__variables_table

    def add_function(self, identifier, parameters, block):
        self.__variables_table[identifier] = {'name': identifier, 'parameters': parameters, 'block': block}
