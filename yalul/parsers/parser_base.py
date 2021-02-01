from yalul.lex.token_type import TokenType


class ParserBase:
    def __init__(self, tokens, current_token):
        """
        Construct a new ExpressionParser object.

        :param tokens: A list of language tokens
        :return: returns parsed expression
        """
        self.tokens = tokens
        self._current_token = current_token

    # TODO: Test here
    def consume(self, token_type):
        current_token = self.tokens[self._current_token.current()]

        if current_token.type != TokenType.EOF or current_token.type != TokenType.END_STATEMENT:
            if current_token.type == token_type:
                self._current_token.increment()
