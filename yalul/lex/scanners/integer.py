from yalul.lex.token_type import TokenType
from yalul.lex.token import Token


class IntegerScanner:
    def __init__(self, current_char, source):
        self.current_char = current_char
        self.source = source

    def create_token(self):
        numbers = []

        while IntegerScanner.is_digit(self.current_char):
            numbers.append(self.current_char)

            self.current_char = self.source.read(1)

        number_string = ''.join(numbers)

        return Token(TokenType.INTEGER, int(number_string))

    @classmethod
    def is_digit(cls, char):
        return '0' <= char <= '9'
