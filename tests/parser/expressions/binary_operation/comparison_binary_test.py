import pytest
from yalul.parser import Parser
from yalul.parse.statements.expressions.binary import Binary
from yalul.parse.statements.expressions.value import Value
from yalul.lex.token import Token
from yalul.lex.token_type import TokenType


class TestParseBinaryComparison:
    """Test parser generating binary comparison operations expressions"""

    def test_parser_run_generates_correct_ast_single_binary_expression_comparison_greater(self):
        """
        Validates if parser is generating a correct AST to a single binary operation comparison greater, like 2 > 1
        """
        tokens = [
            Token(TokenType.INTEGER, 42),
            Token(TokenType.GREATER, ">"),
            Token(TokenType.INTEGER, 1),
            Token(TokenType.EOF, "End of File")
        ]

        ast = Parser(tokens).parse()

        node = ast[0]

        assert type(node) is Binary
        assert node.operator.type == TokenType.GREATER

        assert type(node.left) == Value
        assert node.left.value == 42

        assert node.right.value == 1
        assert type(node.right) == Value

    def test_parser_run_generates_correct_ast_single_binary_expression_comparison_less(self):
        """
        Validates if parser is generating a correct AST to a single binary operation comparison less, like 2 < 1
        """
        tokens = [
            Token(TokenType.INTEGER, 42),
            Token(TokenType.LESS, "<"),
            Token(TokenType.INTEGER, 1),
            Token(TokenType.EOF, "End of File")
        ]

        ast = Parser(tokens).parse()

        node = ast[0]

        assert type(node) is Binary
        assert node.operator.type == TokenType.LESS

        assert type(node.left) == Value
        assert node.left.value == 42

        assert node.right.value == 1
        assert type(node.right) == Value

