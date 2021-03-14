from yalul.lex.token_type import TokenType


class ParserBase:
    def __init__(self, tokens, current_token, errors, parser):
        """
        Construct a new ExpressionParser object.

        :param tokens: A list of language tokens
        :current_token: Current token being read
        :errors: ParseErrors instance
        :return: returns parsed expression
        """
        self.tokens = tokens
        self._current_token = current_token
        self.errors = errors
        self.parser = parser

    # TODO: Test here
    def consume(self, token_type, error_message):
        current_token = self.tokens[self._current_token.current()]

        if current_token.type != TokenType.EOF:
            if current_token.type == token_type:
                token = self.tokens[self._current_token.current()]
                self._current_token.increment()
                return token
            else:
                self.errors.add_error(error_message)

    def current_token(self):
        return self.tokens[self._current_token.current()]
