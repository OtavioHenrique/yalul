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

    def consume(self, token_type, error_message):
        if self.current_token().type != TokenType.EOF:
            if self.current_token().type == token_type:
                token = self.current_token()
                self.token_counter.increment()
                return token
            else:
                self.errors.add_error(error_message)

    def current_token(self):
        return self.tokens[self.token_counter.current()]

    def last_token(self):
        return self.tokens[self.token_counter.current() - 1]
