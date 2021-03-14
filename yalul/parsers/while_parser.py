from yalul.parsers.ast.nodes.statements.block import Block
from yalul.parsers.ast.nodes.statements.expressions.grouping import Grouping
from yalul.parsers.ast.nodes.statements.while_statement import While
from yalul.parsers.block_parser import BlockParser
from yalul.parsers.expression_parser import ExpressionParser
from yalul.parsers.parser_base import ParserBase


class WhileParser(ParserBase):
    """
    Yalul's while statement parser, it parses all whiles
    """

    def __init__(self, tokens, current_token, errors, parser):
        """
        Construct a new WhileParser object.

        :param tokens: A list of language tokens
        :current_token: Current token being read
        :errors: ParseErrors instance
        :return: returns parsed expression
        """
        super().__init__(tokens, current_token, errors, parser)

    def parse(self):
        self._current_token.increment()

        condition_expression = ExpressionParser(self.tokens, self._current_token, self.errors).parse()

        if type(condition_expression) != Grouping:
            self.errors.add_error("Expect a grouping operator with conditions for while")

        block = BlockParser(self.tokens, self._current_token, self.errors, self.parser).parse()

        if type(block) != Block:
            self.errors.add_error("Expect a block after while condition")

        return While(condition_expression, block)
