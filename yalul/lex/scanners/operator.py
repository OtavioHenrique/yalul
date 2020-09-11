from yalul.lex.token_type import TokenType
from yalul.lex.token import Token

OPERATORS = {
    '+': TokenType.SUM,
    '-': TokenType.MINUS,
    '/': TokenType.DIVISION,
    '*': TokenType.MULTIPLY
}


class OperatorScanner:
    def __init__(self, token):
        self.token = token

    @classmethod
    def is_operator(cls, char):
        if char in OPERATORS:
            return True
        else:
            return False

    def create_token(self):
        return Token(OPERATORS.get(self.token), 'OPERATOR')
