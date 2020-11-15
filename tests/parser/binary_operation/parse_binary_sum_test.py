import pytest
from yalul.parser import Parser
from yalul.parse.statements.expressions.binary import Binary
from yalul.parse.statements.expressions.value import Value
from yalul.lex.token import Token
from yalul.lex.token_type import TokenType


class TestParseBinarySum:
    """Test parser generating binary sum operations expressions"""

    def test_parser_run_generates_correct_ast_single_binary_expression_sum(self):
        """
        Validates if parser is generating a correct AST to a single binary operation sum
        """
        tokens = [
            Token(TokenType.INTEGER, 2),
            Token(TokenType.SUM, "+"),
            Token(TokenType.INTEGER, 3),
            Token(TokenType.EOF, "End of File")
        ]

        ast = Parser(tokens).parse()
        ast = ast[0]

        assert type(ast) is Binary
        assert ast.operator.type == TokenType.SUM

        assert type(ast.left) == Value
        assert ast.left.value == 2

        assert ast.right.value == 3
        assert type(ast.right) == Value

    def test_parser_run_generates_correct_ast_complex_binary_expression_sum(self):
        """
        Validates if parser is generating a correct AST to a complex binary operation sum, like 39 + 1 + 2
        """
        tokens = [
            Token(TokenType.INTEGER, 39),
            Token(TokenType.SUM, "+"),
            Token(TokenType.INTEGER, 1),
            Token(TokenType.SUM, "+"),
            Token(TokenType.INTEGER, 2),
            Token(TokenType.EOF, "End of File")
        ]

        ast = Parser(tokens).parse()

        ast = ast[0]

        assert type(ast) is Binary
        assert ast.operator.type is TokenType.SUM

        assert type(ast.left) is Value
        assert ast.left.value == 39

        assert type(ast.right) is Binary
        assert ast.right.operator.type is TokenType.SUM

        assert type(ast.right.left) is Value
        assert ast.right.left.value == 1

        assert type(ast.right.right) is Value
        assert ast.right.right.value == 2