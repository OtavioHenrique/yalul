from yalul.lex.token_type import TokenType
from yalul.lex.token import Token

PAREN = {
    '(': TokenType.LEFT_PAREN,
    ')': TokenType.RIGHT_PAREN
}


class GroupingScanner:
    """
    GroupingScanner is called by Lexer when a paren character is read. It reads the paren and returns a paren Token
    """

    def __init__(self, current_char, source):
        """
        Construct a new GroupingScanner object.

        :params current_char: Current char being read by Lexer
        :param source: Source code being read
        :return: returns nothing
        """
        self.current_char = current_char
        self.source = source

    def create_token(self):
        """
        Read source and creates a new paren token
        """

        token = Token(PAREN.get(self.current_char), "paren")
        self.current_char = self.source.read(1)

        return token

    @classmethod
    def is_paren(cls, char):
        """
        Receives a char and returning if is a paren
        """
        return char == '(' or char == ')'
