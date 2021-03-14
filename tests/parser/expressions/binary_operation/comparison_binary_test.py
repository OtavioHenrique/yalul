from yalul.parser import Parser
from yalul.parsers.ast.nodes.statements.expressions.binary import Binary
from yalul.lex.token import Token
from yalul.lex.token_type import TokenType
from yalul.parsers.ast.nodes.statements.expressions.values.integer import Integer


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
            Token(TokenType.END_STATEMENT, "End of Statement"),
            Token(TokenType.EOF, "End of File")
        ]

        parser_response = Parser(tokens).parse()
        assert len(parser_response.errors()) == 0

        node = parser_response.asts[0]

        assert type(node) is Binary
        assert node.operator.type == TokenType.GREATER

        assert type(node.left) == Integer
        assert node.left.value == 42

        assert node.right.value == 1
        assert type(node.right) == Integer

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

        parser_response = Parser(tokens).parse()

        node = parser_response.asts[0]

        assert type(node) is Binary
        assert node.operator.type == TokenType.LESS

        assert type(node.left) == Integer
        assert node.left.value == 42

        assert node.right.value == 1
        assert type(node.right) == Integer

    def test_parser_run_generates_correct_ast_single_binary_expression_comparison_different(self):
        """
        Validates if parser is generating a correct AST to a single binary operation comparison different, like 2 != 1
        """
        tokens = [
            Token(TokenType.INTEGER, 42),
            Token(TokenType.BANG_EQUAL, "!="),
            Token(TokenType.INTEGER, 1),
            Token(TokenType.EOF, "End of File")
        ]

        parser_response = Parser(tokens).parse()

        node = parser_response.asts[0]

        assert type(node) is Binary
        assert node.operator.type == TokenType.BANG_EQUAL

        assert type(node.left) == Integer
        assert node.left.value == 42

        assert node.right.value == 1
        assert type(node.right) == Integer

    def test_parser_run_generates_correct_ast_single_binary_expression_comparison_equal_equal(self):
        """
        Validates if parser is generating a correct AST to a single binary operation comparison equal, like 2 == 1
        """
        tokens = [
            Token(TokenType.INTEGER, 42),
            Token(TokenType.EQUAL_EQUAL, "=="),
            Token(TokenType.INTEGER, 1),
            Token(TokenType.EOF, "End of File")
        ]

        parser_response = Parser(tokens).parse()

        node = parser_response.asts[0]

        assert type(node) is Binary
        assert node.operator.type == TokenType.EQUAL_EQUAL

        assert type(node.left) == Integer
        assert node.left.value == 42

        assert node.right.value == 1
        assert type(node.right) == Integer

    def test_parser_run_generates_correct_ast_single_binary_expression_comparison_greater_equal(self):
        """
        Validates if parser is generating a correct AST to a single binary operation comparison greater equal, like 2 >= 1
        """
        tokens = [
            Token(TokenType.INTEGER, 42),
            Token(TokenType.GREATER_EQUAL, ">="),
            Token(TokenType.INTEGER, 1),
            Token(TokenType.EOF, "End of File")
        ]

        parser_response = Parser(tokens).parse()

        node = parser_response.asts[0]

        assert type(node) is Binary
        assert node.operator.type == TokenType.GREATER_EQUAL

        assert type(node.left) == Integer
        assert node.left.value == 42

        assert node.right.value == 1
        assert type(node.right) == Integer

    def test_parser_run_generates_correct_ast_single_binary_expression_comparison_less_equal(self):
        """
        Validates if parser is generating a correct AST to a single binary operation comparison greater equal, like 2 <= 1
        """
        tokens = [
            Token(TokenType.INTEGER, 42),
            Token(TokenType.LESS_EQUAL, "<="),
            Token(TokenType.INTEGER, 1),
            Token(TokenType.EOF, "End of File")
        ]

        parser_response = Parser(tokens).parse()

        node = parser_response.asts[0]

        assert type(node) is Binary
        assert node.operator.type == TokenType.LESS_EQUAL

        assert type(node.left) == Integer
        assert node.left.value == 42

        assert node.right.value == 1
        assert type(node.right) == Integer

    def test_parser_run_generates_correct_ast_single_binary_expression_comparison_bang(self):
        """
        Validates if parser is generating a correct AST to a single binary operation comparison bang, like 2 ! 1
        """
        tokens = [
            Token(TokenType.INTEGER, 42),
            Token(TokenType.BANG, "!"),
            Token(TokenType.INTEGER, 1),
            Token(TokenType.EOF, "End of File")
        ]

        parser_response = Parser(tokens).parse()

        node = parser_response.asts[0]

        assert type(node) is Binary
        assert node.operator.type == TokenType.BANG

        assert type(node.left) == Integer
        assert node.left.value == 42

        assert node.right.value == 1
        assert type(node.right) == Integer
