from yalul.lex.token_type import TokenType
from yalul.parsers.ast.nodes.statements.expressions.binary import Binary
from yalul.parsers.ast.nodes.statements.expressions.grouping import Grouping
from yalul.parsers.ast.nodes.statements.expressions.values.boolean import Boolean
from yalul.parsers.ast.nodes.statements.expressions.values.null import Null
from yalul.parsers.ast.nodes.statements.expressions.values.float import Float
from yalul.parsers.ast.nodes.statements.expressions.values.integer import Integer
from yalul.parsers.ast.nodes.statements.expressions.values.string import String
from yalul.parsers.ast.nodes.statements.expressions.variable import Variable
from yalul.parsers.parser_base import ParserBase

TOKEN_TO_VALUES = {
    TokenType.INTEGER: Integer,
    TokenType.STRING: String,
    TokenType.FLOAT: Float,
    TokenType.NULL: Null,
    TokenType.TRUE: Boolean,
    TokenType.FALSE: Boolean
}

UNOPENED_OPERATORS = [TokenType.RIGHT_PAREN]


class ExpressionParser(ParserBase):
    """
    Yalul's expression parser, it parses all kinds of expressions
    """

    def __init__(self, tokens, current_token, errors):
        """
        Construct a new ExpressionParser object.

        :param tokens: A list of language tokens
        :current_token: Current token being read
        :errors: ParseErrors instance
        :return: returns parsed expression
        """
        super().__init__(tokens, current_token, errors)

    def parse(self):
        expression = self.__comparison()
        self.consume(TokenType.END_STATEMENT, "Expected a END OF STATEMENT after expression")

        return expression

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

        token_class = TOKEN_TO_VALUES.get(current_token.type)

        if token_class:
            self._current_token.increment()

            return token_class(current_token.value)
        if current_token.type == TokenType.IDENTIFIER:
            self._current_token.increment()

            return Variable(current_token.value)
        if current_token.type == TokenType.LEFT_PAREN:
            self._current_token.increment()

            expression = self.__comparison()

            self.consume(TokenType.RIGHT_PAREN, "Expected a RIGHT PAREN ) after expression")

            return Grouping(expression)
        if current_token.type in UNOPENED_OPERATORS:
            self.errors.add_error("Expect a open operator for " + str(current_token))
            self._current_token.increment()
        else:
            previous_token = self.tokens[self._current_token.current() - 1]
            self.errors.add_error("Expect Expression after " + str(previous_token))
            self._current_token.increment()
