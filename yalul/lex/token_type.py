from enum import Enum


class TokenType(Enum):
    """
    An enum of the available lex tokens of yalul language
    """
    INTEGER = 1
    SUM = 2
    MINUS = 3
    DIVISION = 4
    MULTIPLY = 5
