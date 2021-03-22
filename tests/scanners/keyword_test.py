import pytest
from pathlib import Path

from yalul.lex.scanners.keyword import KeywordScanner
from yalul.lex.token_type import TokenType


@pytest.fixture(scope='function')
def open_file(request):
    return open(str(Path.cwd()) + "/tests/lex_examples/keywords/" + request.param)


class TestCreateToken:
    @pytest.mark.parametrize('open_file', ['null_example.yalul'], indirect=['open_file'])
    def test_create_null_token(self, open_file):
        char = open_file.read(1)
        token = KeywordScanner(char, open_file).create_token()

        assert token.type == TokenType.NULL
        assert token.value == "null"

    @pytest.mark.parametrize('open_file', ['true_example.yalul'], indirect=['open_file'])
    def test_create_true_token(self, open_file):
        char = open_file.read(1)
        token = KeywordScanner(char, open_file).create_token()

        assert token.type == TokenType.TRUE
        assert token.value == "true"

    @pytest.mark.parametrize('open_file', ['false_example.yalul'], indirect=['open_file'])
    def test_create_false_token(self, open_file):
        char = open_file.read(1)
        token = KeywordScanner(char, open_file).create_token()

        assert token.type == TokenType.FALSE
        assert token.value == "false"

    @pytest.mark.parametrize('open_file', ['variable_example.yalul'], indirect=['open_file'])
    def test_create_variable_token(self, open_file):
        char = open_file.read(1)
        token = KeywordScanner(char, open_file).create_token()

        assert token.type == TokenType.VARIABLE
        assert token.value == "def"

    @pytest.mark.parametrize('open_file', ['if_example.yalul'], indirect=['open_file'])
    def test_create_if_token(self, open_file):
        char = open_file.read(1)
        token = KeywordScanner(char, open_file).create_token()

        assert token.type == TokenType.IF
        assert token.value == "if"

    @pytest.mark.parametrize('open_file', ['else_example.yalul'], indirect=['open_file'])
    def test_create_else_token(self, open_file):
        char = open_file.read(1)
        token = KeywordScanner(char, open_file).create_token()

        assert token.type == TokenType.ELSE
        assert token.value == "else"

    @pytest.mark.parametrize('open_file', ['while_example.yalul'], indirect=['open_file'])
    def test_create_while_token(self, open_file):
        char = open_file.read(1)
        token = KeywordScanner(char, open_file).create_token()

        assert token.type == TokenType.WHILE
        assert token.value == "while"

    @pytest.mark.parametrize('open_file', ['function_example.yalul'], indirect=['open_file'])
    def test_create_function_token(self, open_file):
        char = open_file.read(1)
        token = KeywordScanner(char, open_file).create_token()

        assert token.type == TokenType.FUNCTION
        assert token.value == "func"

    @pytest.mark.parametrize('open_file', ['print_example.yalul'], indirect=['open_file'])
    def test_create_function_token(self, open_file):
        char = open_file.read(1)
        token = KeywordScanner(char, open_file).create_token()

        assert token.type == TokenType.PRINT
        assert token.value == "print"
