from _ast import If

from yalul.lex.token_type import TokenType
from yalul.parsers.ast.nodes.statements.block import Block
from yalul.parsers.ast.nodes.statements.if_statement import If
from yalul.parsers.ast.nodes.statements.expressions.grouping import Grouping
from yalul.parsers.block_parser import BlockParser
from yalul.parsers.expression_parser import ExpressionParser
from yalul.parsers.parser_base import ParserBase


class IfParser(ParserBase):
    """
    Yalul's if statement parser, it parses all ifs
    """

    def __init__(self, tokens, current_token, errors, parser):
        """
        Construct a new IfParser object.

        :param tokens: A list of language tokens
        :current_token: Current token being read
        :errors: ParseErrors instance
        :return: returns parsed expression
        """
        super().__init__(tokens, current_token, errors)
        self.parser = parser

    def parse(self):
        self._current_token.increment()

        condition_expression = ExpressionParser(self.tokens, self._current_token, self.errors).parse()

        if type(condition_expression) != Grouping:
            self.errors.add_error("Expect a grouping operator with conditions for an IF")

        then_block = BlockParser(self.tokens, self._current_token, self.errors, self.parser).parse()

        if type(then_block) != Block:
            self.errors.add_error("Expect a block after if condition")

        else_block = None

        if self.tokens[self._current_token.current()].type == TokenType.ELSE:
            self._current_token.increment()

            else_block = BlockParser(self.tokens, self._current_token, self.errors, self.parser).parse()

        return If(condition_expression, then_block, else_block)
