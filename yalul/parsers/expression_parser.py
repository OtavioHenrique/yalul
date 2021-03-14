from yalul.lex.token_type import TokenType
from yalul.parsers.ast.nodes.statements.expressions.binary import Binary
from yalul.parsers.ast.nodes.statements.expressions.grouping import Grouping
from yalul.parsers.ast.nodes.statements.expressions.return_expression import Return
from yalul.parsers.ast.nodes.statements.expressions.values.boolean import Boolean
from yalul.parsers.ast.nodes.statements.expressions.values.null import Null
from yalul.parsers.ast.nodes.statements.expressions.values.float import Float
from yalul.parsers.ast.nodes.statements.expressions.values.integer import Integer
from yalul.parsers.ast.nodes.statements.expressions.values.string import String
from yalul.parsers.ast.nodes.statements.expressions.var_assignment import VarAssignment
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

UNOPENED_OPERATORS = [TokenType.RIGHT_PAREN, TokenType.RIGHT_BRACE]


class ExpressionParser(ParserBase):
    """
    Yalul's expression parser, it parses all kinds of expressions
    """

    def __init__(self, tokens, token_counter, errors):
        """
        Construct a new ExpressionParser object.

        :tokens: A list of language tokens
        :token_counter: A instance of TokenCounter with current token being read
        :errors: ParseErrors instance
        :return: ExpressionParser object
        """
        super().__init__(tokens, token_counter, errors, None)

    def parse(self):
        """
        Parser func statement

        :return: expression object
        """
        expression = self.__var_assignment()

        if self.tokens[self.token_counter.current() - 1].type != TokenType.RIGHT_BRACE \
                and self.current_token().type != TokenType.LEFT_BRACE:
            self.consume(TokenType.END_STATEMENT, "Expected a END OF STATEMENT after expression")

        return expression

    def __var_assignment(self):
        expression = self.__comparison()

        while self.current_token().type == TokenType.EQUAL:
            identifier = self.tokens[self.token_counter.current() - 1].value

            self.token_counter.increment()

            value = self.__var_assignment()

            expression = VarAssignment(identifier, value)

        return expression

    def __comparison(self):
        expression = self.__addition()

        comparison_tokens = [
            TokenType.GREATER,
            TokenType.LESS,
            TokenType.LESS_EQUAL,
            TokenType.GREATER_EQUAL,
            TokenType.BANG,
            TokenType.BANG_EQUAL,
            TokenType.EQUAL_EQUAL
        ]

        while self.current_token().type in comparison_tokens:
            operator = self.current_token()

            self.token_counter.increment()

            right_expression = self.__comparison()

            expression = Binary(expression, operator, right_expression)

        return expression

    def __addition(self):
        expression = self.__minus()

        while self.current_token().type == TokenType.SUM:
            operator = self.current_token()

            self.token_counter.increment()

            right_expression = self.__addition()

            expression = Binary(expression, operator, right_expression)

        return expression

    def __minus(self):
        expression = self.__multiply()

        while self.current_token().type == TokenType.MINUS:
            operator = self.current_token()

            self.token_counter.increment()

            right_expression = self.__minus()

            expression = Binary(expression, operator, right_expression)

        return expression

    def __multiply(self):
        expression = self.__division()

        while self.current_token().type == TokenType.MULTIPLY:
            operator = self.current_token()

            self.token_counter.increment()

            right_expression = self.__multiply()

            expression = Binary(expression, operator, right_expression)

        return expression

    def __division(self):
        expression = self.__literal()

        while self.current_token().type == TokenType.DIVISION:
            operator = self.current_token()

            self.token_counter.increment()

            right_expression = self.__division()

            expression = Binary(expression, operator, right_expression)

        return expression

    def __literal(self):
        current_token = self.current_token()

        token_class = TOKEN_TO_VALUES.get(current_token.type)

        if token_class:
            self.token_counter.increment()

            return token_class(current_token.value)
        if current_token.type == TokenType.IDENTIFIER:
            self.token_counter.increment()

            return Variable(current_token.value)
        if current_token.type == TokenType.LEFT_PAREN:
            self.token_counter.increment()

            expression = self.__comparison()

            self.consume(TokenType.RIGHT_PAREN, "Expected a RIGHT PAREN ) after expression")

            return Grouping(expression)
        if current_token.type == TokenType.RETURN:
            self.token_counter.increment()

            expression = self.__comparison()

            return Return(expression)
        if current_token.type in UNOPENED_OPERATORS:
            self.errors.add_error("Expect a open operator for " + str(current_token))
            self.token_counter.increment()
        else:
            if self.last_token().type != TokenType.RIGHT_BRACE:
                previous_token = self.last_token()
                self.errors.add_error("Expect Expression after " + str(previous_token))

            self.token_counter.increment()
