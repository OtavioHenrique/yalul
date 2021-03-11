from yalul.lex.token_type import TokenType
from yalul.lex.token import Token

KEYWORDS = {
    'null': TokenType.NULL,
    'true': TokenType.TRUE,
    'false': TokenType.FALSE,
    'def': TokenType.VARIABLE,
    'if': TokenType.IF,
    'else': TokenType.ELSE,
    'while': TokenType.WHILE,
    'return': TokenType.RETURN
}


class KeywordScanner:
    """
    IdentifierScanner is called by Lexer when a char character is read. It reads the identifier and returns its token
    """

    def __init__(self, current_char, source, current_line):
        """
        Construct a new IdentifierScanner object.

        :params current_char: Current char being read by Lexer
        :param source: Source code being read
        :param current_line: current line being read
        :return: returns nothing
        """
        self.current_char = current_char
        self.source = source
        self.current_line = current_line

    def create_token(self):
        """
        Read source and creates a new token of the matching identifier
        """

        chars = []

        while KeywordScanner.is_alpha(self.current_char):
            chars.append(self.current_char)

            self.current_char = self.source.read(1)

        keyword = ''.join(chars)

        if keyword in KEYWORDS:
            return Token(KEYWORDS.get(keyword), keyword)
        else:
            return Token(TokenType.IDENTIFIER, keyword)

    @classmethod
    def is_alpha(cls, char):
        """
        Receives a char and returning if is alpha
        """
        return ('a' <= char <= 'z') or ('A' <= char <= 'Z') or char == '_'
