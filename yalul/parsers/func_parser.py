from yalul.lex.token_type import TokenType
from yalul.parsers.ast.nodes.statements.block import Block
from yalul.parsers.ast.nodes.statements.func import Func
from yalul.parsers.block_parser import BlockParser
from yalul.parsers.parser_base import ParserBase


class FuncParser(ParserBase):
    """
    Yalul's func statement parser, it parses all functions
    """

    def __init__(self, tokens, token_counter, errors, parser):
        """
        Construct a new FuncParser object.

        :param tokens: A list of language tokens
        :token_counter: A instance of TokenCounter with current token being read
        :errors: ParseErrors instance
        :return: FuncParser object
        """
        super().__init__(tokens, token_counter, errors, parser)

    def parse(self):
        """
        Parser func statement

        :return: Func object
        """
        self.token_counter.increment()

        func_identifier = self.current_token().value

        self.token_counter.increment()

        if self.current_token().type != TokenType.LEFT_PAREN:
            self.errors.add_error("Expect a left parenthesis after func identifier")

        self.token_counter.increment()

        func_parameters = self.__parse_parameters()

        self.token_counter.increment()

        block = self.__parse_block()

        return Func(func_identifier, func_parameters, block)

    def __parse_parameters(self):
        parameters = []

        while self.current_token().type != TokenType.RIGHT_PAREN:
            parameters.append(self.current_token())
            self.token_counter.increment()

        return parameters

    def __parse_block(self):
        block = BlockParser(self.tokens, self.token_counter, self.errors, self.parser).parse()

        if type(block) != Block:
            self.errors.add_error("Expect a block after while condition")

        return block
