from yalul.parsers.ast.nodes.statements.expression import Expression


class Variable(Expression):
    def __init__(self, value):
        super().__init__(value)
