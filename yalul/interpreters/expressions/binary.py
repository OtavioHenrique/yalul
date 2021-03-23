from yalul.lex.token_type import TokenType
from yalul.parsers.ast.nodes.statements.expressions.values.boolean import Boolean


class BinaryInterpreter:
    """
    BinaryInterpreter interprets all binary operations expressions
    """

    def __init__(self, operator, left, right, error):
        self.operator = operator
        self.left = left
        self.right = right
        self.error = error

    def execute(self):
        """
        Interpret the binary operation
        """
        try:
            if self.operator == TokenType.SUM:
                return self.left + self.right
            elif self.operator == TokenType.MINUS:
                return self.left - self.right
            elif self.operator == TokenType.DIVISION:
                return self.left / self.right
            elif self.operator == TokenType.MULTIPLY:
                return self.left * self.right
            elif self.operator == TokenType.GREATER:
                return self.greater()
            elif self.operator == TokenType.LESS:
                return self.less()
            elif self.operator == TokenType.EQUAL_EQUAL:
                return self.equal_equal()
            elif self.operator == TokenType.LESS_EQUAL:
                return self.less_equal()
            elif self.operator == TokenType.GREATER_EQUAL:
                return self.greater_equal()
        except TypeError:
            self.error.add(
                'Interpreter Error: Cannot execute BinaryOperation of operator {} between values {} and {}'.format(
                    self.operator, self.left, self.right))

    def equal_equal(self):
        result = self.left == self.right

        if result is True:
            return Boolean('true')
        else:
            return Boolean('false')

    def greater(self):
        result = self.left > self.right

        if result is True:
            return Boolean('true')
        else:
            return Boolean('false')

    def less(self):
        result = self.left < self.right

        if result is True:
            return Boolean('true')
        else:
            return Boolean('false')

    def less_equal(self):
        result = self.left <= self.right

        if result is True:
            return Boolean('true')
        else:
            return Boolean('false')

    def greater_equal(self):
        result = self.left >= self.right

        if result is True:
            return Boolean('true')
        else:
            return Boolean('false')
