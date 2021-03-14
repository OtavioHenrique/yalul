from yalul.lex.token_type import TokenType


class ParserBase:
    def __init__(self, tokens, token_counter, errors, parser):
        """
        Construct a new ExpressionParser object.

        :param tokens: A list of language tokens
        :token_counter: A instance of TokenCounter with current token being read
        :errors: ParseErrors instance
        :return: returns parsed expression
        """
        self.tokens = tokens
        self.token_counter = token_counter
        self.errors = errors
        self.parser = parser

    # TODO: Test here
    def consume(self, token_type, error_message):
        current_token = self.tokens[self.token_counter.current()]

        if current_token.type != TokenType.EOF:
            if current_token.type == token_type:
                token = self.tokens[self.token_counter.current()]
                self.token_counter.increment()
                return token
            else:
                self.errors.add_error(error_message)

    def current_token(self):
        return self.tokens[self.token_counter.current()]
