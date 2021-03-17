from yalul.parsers.ast.nodes.statements.expression import Expression


class FuncCall(Expression):
    def __init__(self, callee, arguments):
        self.callee = callee
        self.arguments = arguments
