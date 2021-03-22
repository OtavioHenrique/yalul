from yalul.parsers.ast.nodes.statements.print import Print
from yalul.parsers.expression_parser import ExpressionParser
from yalul.parsers.parser_base import ParserBase


class PrintParser(ParserBase):
    """
    Yalul's print statement parser, it parses all prints
    """

    def __init__(self, tokens, token_counter, errors, parser):
        """
        Construct a new PrintParser object.

        :param tokens: A list of language tokens
        :token_counter: A instance of TokenCounter with current token being read
        :errors: ParseErrors instance
        :return: WhileParser object
        """
        super().__init__(tokens, token_counter, errors, parser)

    def parse(self):
        """
        Parser Print statement

        :return: Print object
        """
        self.token_counter.increment()

        expression = ExpressionParser(self.tokens, self.token_counter, self.errors).parse()

        return Print(expression)
