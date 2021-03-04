# flake8: noqa: C901

import os

from yalul.lex.scanners.block_scanner import BlockScanner
from yalul.lex.scanners.grouping import GroupingScanner
from yalul.lex.scanners.keyword import KeywordScanner
from yalul.lex.scanners.operator import OperatorScanner
from yalul.lex.scanners.integer import NumbersScanner
from yalul.lex.scanners.comparison_operator import ComparisonOperatorScanner
from yalul.lex.scanners.string import StringScanner
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

        :return: returns a list of tokens
        """
        current_char = self.source.read(1)

        tokens_list = []

        is_at_end = False
        current_line = 0

        while not is_at_end:
            if current_char == ' ':
                current_char = self.source.read(1)
            elif current_char == '\n':
                current_line += 1

                if tokens_list[-1].type != TokenType.END_STATEMENT:
                    tokens_list.append(Token(TokenType.END_STATEMENT, "End of Statement"))

                current_char = self.source.read(1)
            elif current_char == '"':
                string = StringScanner(current_char, self.source).create_token()

                tokens_list.append(string)

                current_char = self.source.read(1)
            elif NumbersScanner.is_digit(current_char):
                scanner = NumbersScanner(current_char, self.source)

                tokens_list.append(scanner.create_token())

                current_char = scanner.current_char
            elif OperatorScanner.is_operator(current_char):
                token = OperatorScanner(current_char).create_token()

                tokens_list.append(token)

                current_char = self.source.read(1)
            elif ComparisonOperatorScanner.is_comparison(current_char):
                scanner = ComparisonOperatorScanner(current_char, self.source)
                token = scanner.create_token()

                tokens_list.append(token)

                current_char = scanner.current_char
            elif GroupingScanner.is_paren(current_char):
                scanner = GroupingScanner(current_char, self.source)
                token = scanner.create_token()

                tokens_list.append(token)

                current_char = scanner.current_char
            elif BlockScanner.is_block(current_char):
                scanner = BlockScanner(current_char, self.source)
                token = scanner.create_token()

                tokens_list.append(token)

                current_char = self.source.read(1)
            elif KeywordScanner.is_alpha(current_char):
                scanner = KeywordScanner(current_char, self.source, current_line)
                token = scanner.create_token()

                tokens_list.append(token)

                current_char = scanner.current_char
            elif current_char == '':
                if self.source.tell() == self.file_size:
                    is_at_end = True
                else:
                    self.source.read(1)
            else:
                tokens_list.append(Token(TokenType.ERROR,
                                         "Unexpected token at line {}, token: {}".format(current_line, current_char)))
                current_char = self.source.read(1)

        if tokens_list[-1].type != TokenType.END_STATEMENT:
            tokens_list.append(Token(TokenType.END_STATEMENT, "End of Statement"))

        tokens_list.append(Token(TokenType.EOF, "End of File"))

        return tokens_list

    def __end_of_file(self):
        return self.source.tell() > self.file_size
