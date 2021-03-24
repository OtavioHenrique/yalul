from yalul.parsers.ast.nodes.statements.expression import Expression
from yalul.parsers.ast.nodes.statements.expressions.values.null import Null


class Variable(Expression):
    def __init__(self, value):
        super().__init__(value)

    def __bool__(self):
        if type(self.value) == Null:
            return False
        else:
            return True
