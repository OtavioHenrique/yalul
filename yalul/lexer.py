import os
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

            if self.__is_digit(current_char):
                numbers = []

                while self.__is_digit(current_char):
                    numbers.append(current_char)

                    current_char = self.source.read(1)

                number_string = ''.join(numbers)

                tokens_list.append(Token(TokenType.INTEGER, int(number_string)))

        return tokens_list

    def __is_digit(self, char):
        return '0' <= char <= '9'

    def __end_of_file(self):
        return self.source.tell() >= self.file_size
