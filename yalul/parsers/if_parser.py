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

    def __init__(self, tokens, token_counter, errors, parser):
        """
        Construct a new IfParser object.

        :param tokens: A list of language tokens
        :token_counter: A instance of TokenCounter with current token being read
        :errors: ParseErrors instance
        :return: IfParser object
        """
        super().__init__(tokens, token_counter, errors, parser)

    def parse(self):
        """
        Parser if statement

        :return: If object
        """
        self.token_counter.increment()

        condition_expression = self.__parse_condition_expression()

        then_block = self.__parse_then_block()

        else_block = self.__parse_else_block()

        return If(condition_expression, then_block, else_block)

    def __parse_condition_expression(self):
        condition_expression = ExpressionParser(self.tokens, self.token_counter, self.errors).parse()

        if type(condition_expression) != Grouping:
            self.errors.add_error("Expect a grouping operator with conditions for an IF")

        return condition_expression

    def __parse_then_block(self):
        then_block = BlockParser(self.tokens, self.token_counter, self.errors, self.parser).parse()

        if type(then_block) != Block:
            self.errors.add_error("Expect a block after if condition")

        return then_block

    def __parse_else_block(self):
        else_block = None

        if self.current_token().type == TokenType.ELSE:
            self.token_counter.increment()

            else_block = BlockParser(self.tokens, self.token_counter, self.errors, self.parser).parse()

            if type(else_block) != Block:
                self.errors.add_error("Expect a block after else condition")

        return else_block
