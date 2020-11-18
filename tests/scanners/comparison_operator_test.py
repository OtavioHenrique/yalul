import pytest
from pathlib import Path
from yalul.lex.scanners.comparison_operator import ComparisonOperatorScanner
from yalul.lex.token_type import TokenType


@pytest.fixture(scope='function')
def open_file(request):
    return open(str(Path.cwd()) + "/tests/lex_examples/" + request.param)


class TestIsComparison:
    def test_when_is_comparison(self):
        assert ComparisonOperatorScanner.is_comparison('>')

    def test_when_isnt_comparison(self):
        assert not ComparisonOperatorScanner.is_comparison('a')


class TestCreateToken:
    @pytest.mark.parametrize('open_file', ['comparison_operators_example.yalul'], indirect=['open_file'])
    def test_create_token(self, open_file):
        char = open_file.read(1)
        token = ComparisonOperatorScanner(char, open_file).create_token()

        assert token.type == TokenType.GREATER
