from yalul.lex.token_type import TokenType
from yalul.lex.token import Token

OPERATORS = {
    '!': TokenType.BANG,
    '>': TokenType.GREATER,
    '<': TokenType.LESS,
    '=': TokenType.EQUAL,
    '!=': TokenType.BANG_EQUAL,
    '==': TokenType.EQUAL_EQUAL,
    '>=': TokenType.GREATER_EQUAL,
    '<=': TokenType.LESS_EQUAL
}


class ComparisonOperatorScanner:
    """
    ComparisonOperatorScanner is called by Lexer when a comparison operator character is read.
    It reads the operator and returns a Comparison Operator Token
    """
    def __init__(self, current_char, source):
        """
        Construct a new OperatorScanner object.

        :params token: Char of the token
        """
        self.current_char = current_char
        self.source = source

    @classmethod
    def is_comparison(cls, char):
        """
        Receives a char and returning if its a operator
        """
        if char in OPERATORS:
            return True
        else:
            return False

    def create_token(self):
        """
        Returns a new Token of the given char
        """
        current_file_pointer_location = self.source.tell()

        next_character = self.source.read(1)

        self.source.seek(current_file_pointer_location)

        if next_character == '=':
            operator = self.current_char + "="

            self.__jump_in_bytes(2)

            return Token(OPERATORS.get(operator), "Comparison Operator")
        else:
            operator = self.current_char

            self.__jump_in_bytes(1)

            return Token(OPERATORS.get(operator), "Comparison Operator")

    def __jump_in_bytes(self, bytes):
        for _ in range(bytes):
            self.current_char = self.source.read(1)
