from enum import Enum


class TokenType(Enum):
    """
    An enum of the available lex tokens of yalul language
    """
    EOF = 0
    INTEGER = 1
    SUM = 2
    MINUS = 3
    DIVISION = 4
    MULTIPLY = 5
    GREATER = 6
    LESS = 7
    EQUAL_EQUAL = 8
    LESS_EQUAL = 9
    GREATER_EQUAL = 10
    BANG = 11
    EQUAL = 12
    BANG_EQUAL = 13
    END_STATEMENT = 14
    STRING = 15
    FLOAT = 16
    NULL = 17
    TRUE = 18
    FALSE = 19
    LEFT_PAREN = 20
    RIGHT_PAREN = 21
    ERROR = 22
    VARIABLE = 23
    IDENTIFIER = 24
    LEFT_BRACE = 25
    RIGHT_BRACE = 26
