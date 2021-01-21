import pytest
from pathlib import Path

from yalul.lex.scanners.string import StringScanner
from yalul.lex.token_type import TokenType


@pytest.fixture(scope='function')
def open_file(request):
    return open(str(Path.cwd()) + "/tests/lex_examples/" + request.param)


class TestCreateToken:
    @pytest.mark.parametrize('open_file', ['string_example.yalul'], indirect=['open_file'])
    def test_create_token(self, open_file):
        char = open_file.read(1)
        token = StringScanner(char, open_file).create_token()

        assert token.type == TokenType.STRING
        assert token.value == "Ola, tudo bem??!@#$"
