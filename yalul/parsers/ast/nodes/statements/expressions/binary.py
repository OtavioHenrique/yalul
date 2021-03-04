from yalul.parsers.ast.nodes.statements.expression import Expression


class Binary(Expression):
    def __init__(self, left, operator, right):
        self.right = right
        self.operator = operator
        self.left = left