from yalul.parsers.ast.nodes.statements.expression import Expression


class Value(Expression):
    def __init__(self, value):
        self.value = value
