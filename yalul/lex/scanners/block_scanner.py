from yalul.lex.token import Token
from yalul.lex.token_type import TokenType

PAREN = {
    '{': TokenType.LEFT_BRACE,
    '}': TokenType.RIGHT_BRACE
}


class BlockScanner:
    """
    BlockScanner is called by Lexer when a brace character is read. It reads the brace and returns a brace Token
    """

    def __init__(self, current_char, source):
        """
        Construct a new BlockScanner object.

        :params current_char: Current char being read by Lexer
        :param source: Source code being read
        :return: BlockScanner object
        """
        self.current_char = current_char
        self.source = source

    def create_token(self):
        """
        Read source and creates a new brace token

        :return: Token object
        """
        token = Token(PAREN.get(self.current_char), "brace")
        self.current_char = self.source.read(1)

        return token

    @classmethod
    def should_lex(cls, char):
        """
        Receives a char and returning if its a left or right brace
        """
        return char == '{' or char == '}'
