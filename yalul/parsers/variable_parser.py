from yalul.lex.token_type import TokenType
from yalul.parsers.ast.nodes.statements.variable_declaration import VariableDeclaration
from yalul.parsers.expression_parser import ExpressionParser
from yalul.parsers.parser_base import ParserBase


class VariableParser(ParserBase):
    """
    Yalul's variable statement parser, it parses all kinds of variables declarations
    """

    def __init__(self, tokens, token_counter, errors, _parser):
        """
        Construct a new VariableParser object.

        :param tokens: A list of language tokens
        :token_counter: A instance of TokenCounter with current token being read
        :errors: ParseErrors instance
        :return: VariableParser object
        """
        super().__init__(tokens, token_counter, errors, _parser)

    def parse(self):
        """
        Parser VariableDeclaration statement

        :return: VariableDeclaration object
        """
        self.token_counter.increment()

        var_name = self.consume(TokenType.IDENTIFIER, "Expected a identifier after def")
        initializer = None

        if self.tokens[self.token_counter.current()].type == TokenType.EQUAL:
            self.token_counter.increment()
            initializer = ExpressionParser(self.tokens, self.token_counter, self.errors).parse()

        return VariableDeclaration(var_name.value, initializer)
