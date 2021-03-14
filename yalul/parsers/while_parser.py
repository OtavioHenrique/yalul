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

    def __init__(self, tokens, token_counter, errors, parser):
        """
        Construct a new WhileParser object.

        :param tokens: A list of language tokens
        :token_counter: A instance of TokenCounter with current token being read
        :errors: ParseErrors instance
        :return: WhileParser object
        """
        super().__init__(tokens, token_counter, errors, parser)

    def parse(self):
        """
        Parser VariableDeclaration statement

        :return: WhileParser object
        """
        self.token_counter.increment()

        condition_expression = self.__parse_condition_expression()

        block = self.__parse_block()

        return While(condition_expression, block)

    def __parse_condition_expression(self):
        condition_expression = ExpressionParser(self.tokens, self.token_counter, self.errors).parse()

        if type(condition_expression) != Grouping:
            self.errors.add_error("Expect a grouping operator with conditions for while")

        return condition_expression

    def __parse_block(self):
        block = BlockParser(self.tokens, self.token_counter, self.errors, self.parser).parse()

        if type(block) != Block:
            self.errors.add_error("Expect a block after while condition")

        return block
