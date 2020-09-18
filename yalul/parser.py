from yalul.lex.token_type import TokenType
from yalul.parse.statements.expressions.value import Value
from yalul.parse.statements.expressions.binary import Binary


class Parser:
    """
    Yalul's own parser, it receives a list of language tokens provided by lexer and output an abstract syntax tree
    """

    def __init__(self, tokens):
        """
        Construct a new Parser object.

        :param source: A opened file
        :return: returns nothing
        """
        self.tokens = tokens
        self._current_token = 0

    def parse(self):
        """
        Returns a new AST
        """
        statements = []

        while not self.__at_end():
            statement = self.__create_statement()

            statements.append(statement)

        return statements

    def __create_statement(self):
        return self.__expression_statement()

    def __expression_statement(self):
        return self.__addition()

    def __addition(self):
        expression = self.__literal()

        while self.tokens[self._current_token].type == TokenType.SUM:
            operator = self.tokens[self._current_token]

            self._current_token += 1

            right_expression = self.__addition()

            expression = Binary(expression, operator, right_expression)

        return expression

    def __literal(self):
        current_token = self.tokens[self._current_token]

        if current_token.type == TokenType.INTEGER:
            self._current_token += 1

            return Value(current_token.value)

    def __at_end(self):
        current_token = self.tokens[self._current_token]

        return current_token.type == TokenType.EOF

    def __next_token(self):
        next_token_index = self._current_token + 1

        next_token = self.tokens[next_token_index]

        return next_token
