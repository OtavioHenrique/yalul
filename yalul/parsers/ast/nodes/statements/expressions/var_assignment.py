from yalul.parsers.ast.nodes.statements.expression import Expression


class VarAssignment(Expression):
    def __init__(self, identifier, value):
        self.identifier = identifier
        super().__init__(value)
