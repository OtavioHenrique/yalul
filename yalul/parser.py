from yalul.lex.token_type import TokenType
from yalul.parsers.block_parser import BlockParser
from yalul.parsers.expression_parser import ExpressionParser
from yalul.parsers.func_parser import FuncParser
from yalul.parsers.if_parser import IfParser
from yalul.parsers.parse_errors import ParseErrors
from yalul.parsers.parse_response import ParseResponse
from yalul.parsers.parser_base import ParserBase
from yalul.parsers.token_counter import TokenCounter
from yalul.parsers.variable_parser import VariableParser
from yalul.parsers.while_parser import WhileParser
from yalul.parsers.abstract_syntax_tree import AbstractSyntaxTree

TOKEN_TO_PARSERS = {
    TokenType.VARIABLE: VariableParser,
    TokenType.LEFT_BRACE: BlockParser,
    TokenType.IF: IfParser,
    TokenType.WHILE: WhileParser,
    TokenType.FUNCTION: FuncParser
}


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
        super().__init__(tokens, TokenCounter(0), ParseErrors([]), None)

    def parse(self):
        """
        Construct new ASTs based on given Lex tokens

        :return: returns an abstract syntax tree (AST)
        """
        statements = []

        while not self.__at_end():
            statement = self.create_statement()

            statements.append(statement)

        ast = AbstractSyntaxTree(statements)
        return ParseResponse(ast, self.errors)

    def create_statement(self):
        parser_class = TOKEN_TO_PARSERS.get(self.current_token().type)

        if parser_class:
            return parser_class(self.tokens, self.token_counter, self.errors, self).parse()
        else:
            return self.__expression_statement()

    def __expression_statement(self):
        return ExpressionParser(self.tokens, self.token_counter, self.errors).parse()

    def __at_end(self):
        current_token = self.current_token()

        return current_token.type == TokenType.EOF
