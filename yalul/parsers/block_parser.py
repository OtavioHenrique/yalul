from yalul.lex.token_type import TokenType
from yalul.parsers.ast.nodes.statements.block import Block
from yalul.parsers.parser_base import ParserBase


class BlockParser(ParserBase):
    """
    Yalul's block statement parser, it parses all blocks
    """

    def __init__(self, tokens, current_token, errors, parser):
        """
        Construct a new BlockParser object.

        :param tokens: A list of language tokens
        :current_token: Current token being read
        :errors: ParseErrors instance
        :return: returns parsed expression
        """
        super().__init__(tokens, current_token, errors)
        self.parser = parser

    def parse(self):
        statements = []

        self._current_token.increment()

        while self.tokens[self._current_token.current()].type != TokenType.RIGHT_BRACE:
            statements.append(self.parser.create_statement())

        self.consume(TokenType.RIGHT_BRACE, 'Expect a RIGHT BRACE } to close a block')

        return Block(statements)
