from yalul.parsers.ast.nodes.statements.expressions.value import Value


class Float(Value):
    def __init__(self, value):
        super().__init__(value)
