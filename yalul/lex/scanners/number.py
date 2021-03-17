from yalul.lex.token_type import TokenType
from yalul.lex.token import Token


class NumbersScanner:
    """
    IntegerScanner is called by Lexer when a digit character is read. It reads the integer and returns a Integer Token
    """

    def __init__(self, current_char, source):
        """
        Construct a new IntegerScanner object.

        :params current_char: Current char being read by Lexer
        :param source: Source code being read
        :return: NumbersScanner object
        """
        self.current_char = current_char
        self.source = source

    def create_token(self):
        """
        Read source and creates a new integer token

        :returns: Token object
        """
        numbers = []
        is_float = False

        while NumbersScanner.should_lex(self.current_char) or self.current_char == '.' or self.current_char == '-':
            numbers.append(self.current_char)

            if self.current_char == '.':
                is_float = True

            self.current_char = self.source.read(1)

        number_string = ''.join(numbers)

        if is_float is True:
            return Token(TokenType.FLOAT, float(number_string))
        else:
            return Token(TokenType.INTEGER, int(number_string))

    @classmethod
    def should_lex(cls, char):
        """
        Receives a char and returning if its a digit
        """
        return '0' <= char <= '9'
