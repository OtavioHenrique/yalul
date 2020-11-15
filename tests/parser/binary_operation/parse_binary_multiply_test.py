import pytest
from yalul.parser import Parser
from yalul.parse.statements.expressions.binary import Binary
from yalul.parse.statements.expressions.value import Value
from yalul.lex.token import Token
from yalul.lex.token_type import TokenType


class TestParseBinaryMultiply:
    """Test parser generating binary multiply operations expressions"""

    def test_parser_run_generates_correct_ast_single_binary_expression_multiply(self):
        """
        Validates if parser is generating a correct AST to a single binary operation multiply, like 2 * 1
        """
        tokens = [
            Token(TokenType.INTEGER, 42),
            Token(TokenType.MULTIPLY, "*"),
            Token(TokenType.INTEGER, 1),
            Token(TokenType.EOF, "End of File")
        ]

        ast = Parser(tokens).parse()

        ast = ast[0]

        assert type(ast) is Binary
        assert ast.operator.type == TokenType.MULTIPLY

        assert type(ast.left) == Value
        assert ast.left.value == 42

        assert ast.right.value == 1
        assert type(ast.right) == Value
