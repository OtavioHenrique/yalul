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
        token = KeywordScanner(char, open_file, 0).create_token()

        assert token.type == TokenType.NULL
        assert token.value == "Identifier"

    @pytest.mark.parametrize('open_file', ['true_example.yalul'], indirect=['open_file'])
    def test_create_true_token(self, open_file):
        char = open_file.read(1)
        token = KeywordScanner(char, open_file, 0).create_token()

        assert token.type == TokenType.TRUE
        assert token.value == "Identifier"

    @pytest.mark.parametrize('open_file', ['false_example.yalul'], indirect=['open_file'])
    def test_create_false_token(self, open_file):
        char = open_file.read(1)
        token = KeywordScanner(char, open_file, 0).create_token()

        assert token.type == TokenType.FALSE
        assert token.value == "Identifier"
