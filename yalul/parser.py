from yalul.lex.token_type import TokenType
from yalul.parsers.block_parser import BlockParser
from yalul.parsers.expression_parser import ExpressionParser
from yalul.parsers.func_parser import FuncParser
from yalul.parsers.if_parser import IfParser
from yalul.parsers.parse_errors import ParseErrors
from yalul.parsers.parse_response import ParseResponse
from yalul.parsers.parser_base import ParserBase
from yalul.parsers.variable_parser import VariableParser
from yalul.parsers.while_parser import WhileParser


class Token:
    def __init__(self, current):
        self.current_token = current

    def current(self):
        return self.current_token

    def increment(self):
        self.current_token += 1
        return self.current_token


class Parser(ParserBase):
    """
    Yalul's own parser, it receives a list of language tokens provided by lexer and output an abstract syntax tree
    """

    def __init__(self, tokens):
        """
        Construct a new Parser object.

        :param tokens: A list of language tokens
        :return: returns nothing
        """
        super().__init__(tokens, Token(0), ParseErrors([]))

    def parse(self):
        """
        Returns a new AST

        :return: returns an abstract syntax tree (AST)
        """
        statements = []

        while not self.__at_end():
            statement = self.create_statement()

            statements.append(statement)

        return ParseResponse(statements, self.errors)

    def create_statement(self):
        if self.current_token().type == TokenType.VARIABLE:
            return VariableParser(self.tokens, self._current_token, self.errors).parse()
        if self.current_token().type == TokenType.LEFT_BRACE:
            return BlockParser(self.tokens, self._current_token, self.errors, self).parse()
        if self.current_token().type == TokenType.IF:
            return IfParser(self.tokens, self._current_token, self.errors, self).parse()
        if self.current_token().type == TokenType.WHILE:
            return WhileParser(self.tokens, self._current_token, self.errors, self).parse()
        if self.current_token().type == TokenType.FUNCTION:
            return FuncParser(self.tokens, self._current_token, self.errors, self).parse()
        else:
            return self.__expression_statement()

    def __expression_statement(self):
        return ExpressionParser(self.tokens, self._current_token, self.errors).parse()

    def __at_end(self):
        current_token = self.current_token()

        return current_token.type == TokenType.EOF
