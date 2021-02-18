from yalul.lex.token_type import TokenType
from yalul.parsers.ast.nodes.statements.variable import Variable
from yalul.parsers.expression_parser import ExpressionParser
from yalul.parsers.parser_base import ParserBase


class VariableParser(ParserBase):
    """
    Yalul's variable statement parser, it parses all kinds of variables declarations
    """

    def __init__(self, tokens, current_token, errors):
        """
        Construct a new VariableParser object.

        :param tokens: A list of language tokens
        :current_token: Current token being read
        :errors: ParseErrors instance
        :return: returns parsed expression
        """
        super().__init__(tokens, current_token, errors)

    def parse(self):
        self._current_token.increment()

        var_name = self.consume(TokenType.IDENTIFIER, "Expected a identifier after def")
        initializer = None

        if self.tokens[self._current_token.current()].type == TokenType.EQUAL:
            self._current_token.increment()
            initializer = ExpressionParser(self.tokens, self._current_token, self.errors).parse()

        self.consume(TokenType.END_STATEMENT, "Expected a end of statement after variable declaration")

        return Variable(var_name.value, initializer)
