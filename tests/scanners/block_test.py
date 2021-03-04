import pytest
from pathlib import Path

from yalul.lex.scanners.block_scanner import BlockScanner
from yalul.lex.token_type import TokenType


@pytest.fixture(scope='function')
def open_file(request):
    return open(str(Path.cwd()) + "/tests/lex_examples/" + request.param)


class TestIsBlock:
    def test_when_is_block(self):
        assert BlockScanner.is_block('{')
        assert BlockScanner.is_block('}')

    def test_when_isnt_block(self):
        assert not BlockScanner.is_block('a')


class TestCreateToken:
    @pytest.mark.parametrize('open_file', ['block_example.yalul'], indirect=['open_file'])
    def test_create_token_integer(self, open_file):
        char = open_file.read(1)
        token = BlockScanner(char, open_file).create_token()

        assert token.type == TokenType.LEFT_BRACE
        assert token.value == 'brace'
