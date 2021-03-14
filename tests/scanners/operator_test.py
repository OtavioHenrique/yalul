from pathlib import Path

import pytest

from yalul.lex.scanners.operator import OperatorScanner
from yalul.lex.token_type import TokenType


@pytest.fixture(scope='function')
def open_file(request):
    return open(str(Path.cwd()) + "/tests/lex_examples/" + request.param)


class TestIsOperator:
    def test_when_is_operator(self):
        operators = ['+', '-', '/', '*']

        for operator in operators:
            assert OperatorScanner.should_lex(operator)

    def test_when_isnt_operator(self):
        assert not OperatorScanner.should_lex('a')


class TestCreateToken:
    @pytest.mark.parametrize('open_file', ['operators_example.yalul'], indirect=['open_file'])
    def test_create_token(self, open_file):
        char = open_file.read(1)
        token = OperatorScanner(char, open_file).create_token()

        assert token.type == TokenType.SUM
        assert token.value == 'OPERATOR'
