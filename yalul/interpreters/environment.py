class Environment:
    def __init__(self):
        self.environment_table = {}

    def add_variable(self, identifier, value):
        self.environment_table[identifier] = value

    def get_variable(self, identifier):
        return self.environment_table[identifier]

    def show_environment_table(self):
        return self.environment_table
