from yalul.lex.token_type import TokenType
from yalul.parsers.expression_parse import ExpressionParser
from yalul.parsers.parse_errors import ParseErrors


# TODO: Test here
from yalul.parsers.parse_response import ParseResponse


class Token:
    def __init__(self, current):
        self.current_token = current

    def current(self):
        return self.current_token

    def increment(self):
        self.current_token += 1
        return self.current_token


class Parser:
    """
    Yalul's own parser, it receives a list of language tokens provided by lexer and output an abstract syntax tree
    """

    def __init__(self, tokens):
        """
        Construct a new Parser object.

        :param tokens: A list of language tokens
        :return: returns an abstract syntax tree (AST)
        """
        self.tokens = tokens
        self._current_token = Token(0)
        self.errors = ParseErrors()

    def parse(self):
        """
        Returns a new AST
        """
        statements = []

        while not self.__at_end():
            statement = self.__create_statement()

            statements.append(statement)

        return ParseResponse(statements, self.errors)

    def __create_statement(self):
        return self.__expression_statement()

    def __expression_statement(self):
        return ExpressionParser(self.tokens, self._current_token, self.errors).parse()

    def __at_end(self):
        current_token = self.tokens[self._current_token.current()]

        return current_token.type == TokenType.EOF
