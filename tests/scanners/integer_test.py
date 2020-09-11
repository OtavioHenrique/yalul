import pytest
from pathlib import Path
from yalul.lex.scanners.integer import IntegerScanner
from yalul.lex.token_type import TokenType


@pytest.fixture(scope='function')
def open_file(request):
    return open(str(Path.cwd()) + "/tests/lex_examples/" + request.param)


class TestIsDigit:
    def test_when_is_digit(self):
        assert IntegerScanner.is_digit('6')

    def test_when_isnt_digit(self):
        assert not IntegerScanner.is_digit('a')


class TestCreateToken:
    @pytest.mark.parametrize('open_file', ['integers_example.yalul'], indirect=['open_file'])
    def test_create_token(self, open_file):
        char = open_file.read(1)
        token = IntegerScanner(char, open_file).create_token()

        assert token.type == TokenType.INTEGER
        assert token.value == 42
