from yalul.lex.token_type import TokenType
from yalul.parsers.ast.nodes.statements.block import Block
from yalul.parsers.parser_base import ParserBase


class BlockParser(ParserBase):
    """
    Yalul's block statement parser, it parses all blocks
    """

    def __init__(self, tokens, token_counter, errors, parser):
        """
        Construct a new BlockParser object.

        :param tokens: A list of language tokens
        :token_counter: A instance of TokenCounter with current token being read
        :errors: ParseErrors instance
        :return: BlockParser object
        """
        super().__init__(tokens, token_counter, errors, parser)

    def parse(self):
        """
        Parser block statement

        :return: Block object
        """
        self.token_counter.increment()

        block_statements = self.__parse_block_statements()

        self.consume(TokenType.RIGHT_BRACE, 'Expect a RIGHT BRACE } to close a block')

        return Block(block_statements)

    def __parse_block_statements(self):
        statements = []

        while self.current_token().type != TokenType.RIGHT_BRACE:
            statements.append(self.parser.create_statement())

        return statements
