from yalul.lex.token_type import TokenType
from yalul.lex.token import Token

IDENTIFIERS = {
    'null': TokenType.NULL,
    'true': TokenType.TRUE,
    'false': TokenType.FALSE
}


class KeywordScanner:
    """
    IdentifierScanner is called by Lexer when a char character is read. It reads the identifier and returns its token
    """

    def __init__(self, current_char, source):
        """
        Construct a new IdentifierScanner object.

        :params current_char: Current char being read by Lexer
        :param source: Source code being read
        :return: returns nothing
        """
        self.current_char = current_char
        self.source = source

    def create_token(self):
        """
        Read source and creates a new token of the matching identifier
        """

        chars = []

        while KeywordScanner.is_alpha(self.current_char):
            chars.append(self.current_char)

            self.current_char = self.source.read(1)

        identifier = ''.join(chars)

        return Token(IDENTIFIERS.get(identifier), "Identifier")

    @classmethod
    def is_alpha(cls, char):
        """
        Receives a char and returning if is alpha
        """
        return ('a' <= char <= 'z') or ('A' <= char <= 'Z') or char == '_'
