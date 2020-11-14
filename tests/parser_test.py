import pytest
from yalul.parser import Parser
from yalul.parse.statements.expressions.binary import Binary
from yalul.parse.statements.expressions.value import Value
from yalul.lex.token import Token
from yalul.lex.token_type import TokenType


class TestParserBinary:
    """Test parser generating binary operations expressions"""

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

    def test_parser_run_generates_correct_ast_complex_binary_expression_with_multi_precedence(self):
        """
        Validates if parser is generating a correct AST to a binary expression with multi precedence, like 39 * 2 + 42
        """
        tokens = [
            Token(TokenType.INTEGER, 39),
            Token(TokenType.MULTIPLY, "*"),
            Token(TokenType.INTEGER, 2),
            Token(TokenType.SUM, "+"),
            Token(TokenType.INTEGER, 42),
            Token(TokenType.EOF, "End of File")
        ]

        ast = Parser(tokens).parse()

        ast = ast[0]

        assert type(ast) is Binary
        assert ast.operator.type is TokenType.SUM

        assert type(ast.left) is Binary
        assert ast.left.operator.type is TokenType.MULTIPLY

        assert type(ast.left.left) is Value
        assert ast.left.left.value == 39

        assert type(ast.left.right) is Value
        assert ast.left.right.value == 2

        assert type(ast.right) is Value
        assert ast.right.value is 42


