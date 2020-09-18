import os

from yalul.lex.scanners.operator import OperatorScanner
from yalul.lex.scanners.integer import IntegerScanner
from yalul.lex.token import Token
from yalul.lex.token_type import TokenType


class Lexer:
    """
    Yalul's own Lexer.

    This class has as it main objective receive a source code, scan it and produce a list of language tokens.
    """

    def __init__(self, source):
        """
        Construct a new Lexer object.

        :param source: A opened file
        :return: returns nothing
        """
        self.source = source
        self.file_size = os.fstat(source.fileno()).st_size

    def run(self):
        """
        Return a list of tokens for the source
        """
        current_char = self.source.read(1)

        tokens_list = []

        while not self.__end_of_file():
            if current_char == ' ' or current_char == '\n':
                current_char = self.source.read(1)

            if IntegerScanner.is_digit(current_char):
                scanner = IntegerScanner(current_char, self.source)

                tokens_list.append(scanner.create_token())

                current_char = scanner.current_char

            if OperatorScanner.is_operator(current_char):
                token = OperatorScanner(current_char).create_token()

                tokens_list.append(token)

                current_char = self.source.read(1)

        tokens_list.append(Token(TokenType.EOF, "End of File"))

        return tokens_list

    def __end_of_file(self):
        return self.source.tell() >= self.file_size
