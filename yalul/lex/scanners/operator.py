from yalul.lex.scanners.number import NumbersScanner
from yalul.lex.token_type import TokenType
from yalul.lex.token import Token

OPERATORS = {
    '+': TokenType.SUM,
    '-': TokenType.MINUS,
    '/': TokenType.DIVISION,
    '*': TokenType.MULTIPLY
}


class OperatorScanner:
    """
    OperatorScanner is called by Lexer when a operator character is read. It reads the operator and returns a Operator Token
    """
    def __init__(self, current_char, source):
        """
        Construct a new OperatorScanner object.

        :params token: Char of the token
        :params source: Source being read
        :returns: OperatorScanner object
        """
        self.current_char = current_char
        self.source = source

    @classmethod
    def should_lex(cls, char):
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
        initial_file_pointer_location = self.source.tell()
        token = None
        next_character = self.source.read(1)

        self.source.seek(initial_file_pointer_location)

        if NumbersScanner.should_lex(next_character):
            scanner = NumbersScanner(self.current_char, self.source)
            token = scanner.create_token()

            self.current_char = scanner.current_char
        else:
            token = Token(OPERATORS.get(self.current_char), 'OPERATOR')
            self.current_char = self.source.read(1)

        return token
