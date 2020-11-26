from yalul.parser import Parser
from yalul.parsers.ast.nodes.statements.expressions.binary import Binary
from yalul.parsers.ast.nodes.statements.expressions.value import Value
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

    def test_parser_run_generates_correct_ast_complex_binary_expression_multiply(self):
        """
        Validates if parser is generating a correct AST to a complex binary operation sum, like 39 * 1 * 2
        """
        tokens = [
            Token(TokenType.INTEGER, 39),
            Token(TokenType.MULTIPLY, "*"),
            Token(TokenType.INTEGER, 1),
            Token(TokenType.MULTIPLY, "*"),
            Token(TokenType.INTEGER, 2),
            Token(TokenType.EOF, "End of File")
        ]

        ast = Parser(tokens).parse()

        ast = ast[0]

        assert type(ast) is Binary
        assert ast.operator.type is TokenType.MULTIPLY

        assert type(ast.left) is Value
        assert ast.left.value == 39

        assert type(ast.right) is Binary
        assert ast.right.operator.type is TokenType.MULTIPLY

        assert type(ast.right.left) is Value
        assert ast.right.left.value == 1

        assert type(ast.right.right) is Value
        assert ast.right.right.value == 2
