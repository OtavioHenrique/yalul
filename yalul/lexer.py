import os
from yalul.lex.token import Token
from yalul.lex.token_type import TokenType


class Lexer:
    def __init__(self, source):
        self.source = source
        self.file_size = os.fstat(source.fileno()).st_size

    def run(self):
        current_char = self.source.read(1)

        tokens_list = []

        while not self.__end_of_file(current_char):
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

    def __end_of_file(self, char):
        return self.source.tell() >= self.file_size
