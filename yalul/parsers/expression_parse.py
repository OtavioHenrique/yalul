from yalul.lex.token_type import TokenType
from yalul.parsers.ast.nodes.statements.expressions.binary import Binary
from yalul.parsers.ast.nodes.statements.expressions.value import Value


class ExpressionParser:
    """
    Yalul's expression parser, it parses all kinds of expressions
    """

    def __init__(self, tokens, current_token):
        """
        Construct a new ExpressionParser object.

        :param tokens: A list of language tokens
        :return: returns parsed expression
        """
        self.tokens = tokens
        self._current_token = current_token

    def parse(self):
        return self.__comparison()

    def __comparison(self):
        expression = self.__addition()

        comparison_tokens = [
            TokenType.GREATER,
            TokenType.LESS,
            TokenType.LESS_EQUAL,
            TokenType.GREATER_EQUAL,
            TokenType.BANG,
            TokenType.EQUAL,
            TokenType.BANG_EQUAL,
            TokenType.EQUAL_EQUAL
        ]

        while self.tokens[self._current_token.current()].type in comparison_tokens:
            operator = self.tokens[self._current_token.current()]

            self._current_token.increment()

            right_expression = self.__comparison()

            expression = Binary(expression, operator, right_expression)

        return expression

    def __addition(self):
        expression = self.__minus()

        while self.tokens[self._current_token.current()].type == TokenType.SUM:
            operator = self.tokens[self._current_token.current()]

            self._current_token.increment()

            right_expression = self.__addition()

            expression = Binary(expression, operator, right_expression)

        return expression

    def __minus(self):
        expression = self.__multiply()

        while self.tokens[self._current_token.current()].type == TokenType.MINUS:
            operator = self.tokens[self._current_token.current()]

            self._current_token.increment()

            right_expression = self.__minus()

            expression = Binary(expression, operator, right_expression)

        return expression

    def __multiply(self):
        expression = self.__division()

        while self.tokens[self._current_token.current()].type == TokenType.MULTIPLY:
            operator = self.tokens[self._current_token.current()]

            self._current_token.increment()

            right_expression = self.__multiply()

            expression = Binary(expression, operator, right_expression)

        return expression

    def __division(self):
        expression = self.__literal()

        while self.tokens[self._current_token.current()].type == TokenType.DIVISION:
            operator = self.tokens[self._current_token.current()]

            self._current_token.increment()

            right_expression = self.__division()

            expression = Binary(expression, operator, right_expression)

        return expression

    def __literal(self):
        current_token = self.tokens[self._current_token.current()]

        if current_token.type == TokenType.INTEGER:
            self._current_token.increment()

            return Value(current_token.value)
        else:
            return current_token
