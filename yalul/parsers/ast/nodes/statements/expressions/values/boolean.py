from yalul.parsers.ast.nodes.statements.expressions.value import Value


class Boolean(Value):
    def __init__(self, value):
        super().__init__(value)

    def __str__(self):
        return self.value

    def __bool__(self):
        if self.value == 'true':
            return True
        else:
            return False
