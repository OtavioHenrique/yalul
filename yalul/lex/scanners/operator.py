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
        token = Token(OPERATORS.get(self.current_char), 'OPERATOR')
        self.current_char = self.source.read(1)

        return token
