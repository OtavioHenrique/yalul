import pytest
from yalul.parser import Parser
from yalul.parse.statements.expressions.binary import Binary
from yalul.parse.statements.expressions.value import Value
from yalul.lex.token import Token
from yalul.lex.token_type import TokenType


class TestParseBinaryDivision:
    """Test parser generating binary division operations expressions"""

    def test_parser_run_generates_correct_ast_single_binary_expression_division(self):
        """
        Validates if parser is generating a correct AST to a single binary operation division
        """
        tokens = [
            Token(TokenType.INTEGER, 10),
            Token(TokenType.DIVISION, "/"),
            Token(TokenType.INTEGER, 2),
            Token(TokenType.EOF, "End of File")
        ]

        ast = Parser(tokens).parse()
        ast = ast[0]

        assert type(ast) is Binary
        assert ast.operator.type == TokenType.DIVISION

        assert type(ast.left) == Value
        assert ast.left.value == 10

        assert ast.right.value == 2
        assert type(ast.right) == Value