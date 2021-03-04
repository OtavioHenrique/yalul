from yalul.lex.scanners.operator import OperatorScanner
from yalul.lex.token_type import TokenType


class TestIsOperator:
    def test_when_is_operator(self):
        operators = ['+', '-', '/', '*']

        for operator in operators:
            assert OperatorScanner.is_operator(operator)

    def test_when_isnt_operator(self):
        assert not OperatorScanner.is_operator('a')


class TestCreateToken:
    def test_create_token(self):
        scanner = OperatorScanner('+')

        assert scanner.create_token().type == TokenType.SUM
        assert scanner.create_token().value == 'OPERATOR'
