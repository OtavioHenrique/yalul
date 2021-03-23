from yalul.lex.token_type import TokenType


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
                return self.left > self.right
            elif self.operator == TokenType.LESS:
                return self.left < self.right
            elif self.operator == TokenType.EQUAL_EQUAL:
                return self.left == self.right
            elif self.operator == TokenType.LESS_EQUAL:
                return self.left <= self.right
            elif self.operator == TokenType.GREATER_EQUAL:
                return self.left >= self.right
        except TypeError:
            self.error.add(
                'Interpreter Error: Cannot execute BinaryOperation of operator {} between values {} and {}'.format(
                    self.operator, self.left, self.right))
