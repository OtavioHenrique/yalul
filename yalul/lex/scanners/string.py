from yalul.lex.token_type import TokenType
from yalul.lex.token import Token


class StringScanner:
    """
    StringScanner is called by Lexer when a string character is read. It reads the string and returns a String Token
    """

    def __init__(self, current_char, source):
        """
        Construct a new StingScanner object.

        :params current_char: Current char being read by Lexer
        :param source: Source code being read
        :return: returns nothing
        """
        self.current_char = current_char
        self.source = source

    def create_token(self):
        """
        Read source and creates a new string token
        """
        self.current_char = self.source.read(1)

        chars = []

        while self.current_char != '"':
            chars.append(self.current_char)

            self.current_char = self.source.read(1)

        string = ''.join(chars)

        return Token(TokenType.STRING, string)
