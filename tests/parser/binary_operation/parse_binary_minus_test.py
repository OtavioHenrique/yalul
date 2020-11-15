import pytest
from yalul.parser import Parser
from yalul.parse.statements.expressions.binary import Binary
from yalul.parse.statements.expressions.value import Value
from yalul.lex.token import Token
from yalul.lex.token_type import TokenType


class TestParseBinaryMinus:
    """Test parser generating binary minus operations expressions"""

    def test_parser_run_generates_correct_ast_single_binary_expression_minus(self):
        """
        Validates if parser is generating a correct AST to a single binary operation minus
        """
        tokens = [
            Token(TokenType.INTEGER, 5),
            Token(TokenType.MINUS, "-"),
            Token(TokenType.INTEGER, 3),
            Token(TokenType.EOF, "End of File")
        ]

        ast = Parser(tokens).parse()
        ast = ast[0]

        assert type(ast) is Binary
        assert ast.operator.type == TokenType.MINUS

        assert type(ast.left) == Value
        assert ast.left.value == 5

        assert ast.right.value == 3
        assert type(ast.right) == Value