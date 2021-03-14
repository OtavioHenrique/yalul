import pytest
from pathlib import Path
from yalul.lex.scanners.grouping import GroupingScanner
from yalul.lex.token_type import TokenType


@pytest.fixture(scope='function')
def open_file(request):
    return open(str(Path.cwd()) + "/tests/lex_examples/" + request.param)


class TestShouldLex:
    def test_when_is_left_paren(self):
        assert GroupingScanner.should_lex('(')

    def test_when_is_right_paren(self):
        assert GroupingScanner.should_lex(')')

    def test_when_isnt_paren(self):
        assert not GroupingScanner.should_lex('a')


class TestCreateToken:
    @pytest.mark.parametrize('open_file', ['grouping_example.yalul'], indirect=['open_file'])
    def test_create_token(self, open_file):
        char = open_file.read(1)
        scanner = GroupingScanner(char, open_file)

        assert scanner.create_token().type == TokenType.LEFT_PAREN
        assert scanner.create_token().type == TokenType.RIGHT_PAREN
