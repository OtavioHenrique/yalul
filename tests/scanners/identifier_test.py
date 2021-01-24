import pytest
from pathlib import Path

from yalul.lex.scanners.identifier import IdentifierScanner
from yalul.lex.token_type import TokenType


@pytest.fixture(scope='function')
def open_file(request):
    return open(str(Path.cwd()) + "/tests/lex_examples/identifiers/" + request.param)


class TestCreateToken:
    @pytest.mark.parametrize('open_file', ['null_example.yalul'], indirect=['open_file'])
    def test_create_null_token(self, open_file):
        char = open_file.read(1)
        token = IdentifierScanner(char, open_file).create_token()

        assert token.type == TokenType.NULL
        assert token.value == "Identifier"
