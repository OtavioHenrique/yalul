import pytest
from pathlib import Path
from yalul.lex.scanners.integer import NumbersScanner
from yalul.lex.token_type import TokenType


@pytest.fixture(scope='function')
def open_file(request):
    return open(str(Path.cwd()) + "/tests/lex_examples/" + request.param)


class TestIsDigit:
    def test_when_is_digit(self):
        assert NumbersScanner.is_digit('6')

    def test_when_isnt_digit(self):
        assert not NumbersScanner.is_digit('a')


class TestCreateToken:
    @pytest.mark.parametrize('open_file', ['integers_example.yalul'], indirect=['open_file'])
    def test_create_token_integer(self, open_file):
        char = open_file.read(1)
        token = NumbersScanner(char, open_file).create_token()

        assert token.type == TokenType.INTEGER
        assert token.value == 42

    @pytest.mark.parametrize('open_file', ['float_example.yalul'], indirect=['open_file'])
    def test_create_token_float(self, open_file):
        char = open_file.read(1)
        token = NumbersScanner(char, open_file).create_token()

        assert token.type == TokenType.FLOAT
        assert token.value == 3.14159