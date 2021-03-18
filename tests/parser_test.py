from yalul.parser import Parser
from yalul.parsers.ast.nodes.statements.expressions.binary import Binary
from yalul.lex.token import Token
from yalul.lex.token_type import TokenType
from yalul.parsers.ast.nodes.statements.expressions.values.integer import Integer


class TestParserBinary:
    """Test parser generating binary operations expressions"""

    def test_parser_run_generates_correct_ast_complex_binary_expression_with_multi_precedence(self):
        """
        Validates if parser is generating a correct AST to a binary expressions with multi precedence, like 39 * 2 + 42
        """
        tokens = [
            Token(TokenType.INTEGER, 39),
            Token(TokenType.MULTIPLY, "*"),
            Token(TokenType.INTEGER, 2),
            Token(TokenType.SUM, '+'),
            Token(TokenType.INTEGER, 42),
            Token(TokenType.END_STATEMENT, 'End of Statement'),
            Token(TokenType.EOF, 'End of File')
        ]

        parser_response = Parser(tokens).parse()

        asts = parser_response.ast.statements

        ast = asts[0]

        assert type(ast) is Binary
        assert ast.operator.type is TokenType.SUM

        assert type(ast.left) is Binary
        assert ast.left.operator.type is TokenType.MULTIPLY

        assert type(ast.left.left) is Integer
        assert ast.left.left.value == 39

        assert type(ast.left.right) is Integer
        assert ast.left.right.value == 2

        assert type(ast.right) is Integer
        assert ast.right.value == 42


class TestParserGenerateErrors:
    """Test parser generating correct parser errors"""

    def test_parser_run_generates_correct_parser_errors(self):
        """
        Validates if parser is generating a correct parser errors
        """
        tokens = [
            Token(TokenType.INTEGER, 39),
            Token(TokenType.MULTIPLY, '*'),
            Token(TokenType.LEFT_PAREN, 'Left Paren'),
            Token(TokenType.INTEGER, 41),
            Token(TokenType.SUM, '+'),
            Token(TokenType.INTEGER, 1),
            Token(TokenType.END_STATEMENT, 'End of Statement'),
            Token(TokenType.EOF, 'End of File')
        ]

        parser_response = Parser(tokens).parse()

        errors = parser_response.errors()

        assert errors[0] == 'Expected a RIGHT PAREN ) after expression'


class TestParserGenerateUnfinishedExpressionErrors:
    """Test parser generating correct parser errors"""

    def test_parse_run_generates_correct_error_unfinished_expression(self):
        """
        Validates if parser if generating correct error to unfinished expressions
        """
        tokens = [
            Token(TokenType.INTEGER, 39),
            Token(TokenType.MULTIPLY, '*'),
            Token(TokenType.INTEGER, 41),
            Token(TokenType.SUM, '+'),
            Token(TokenType.END_STATEMENT, 'End of Statement'),
            Token(TokenType.EOF, 'End of File')
        ]

        parser_response = Parser(tokens).parse()

        errors = parser_response.errors()
        assert errors[0] == 'Expect Expression after TokenType.SUM, Value: +'


class TestParserGenerateUnopenedOperatorError:
    """Test parser generating correct parser errors"""

    def test_parse_run_generates_correct_error_unopened_operators_right_paren(self):
        """
        Validates if parser if generating correct error to unopened operators
        """
        tokens = [
            Token(TokenType.INTEGER, 39),
            Token(TokenType.MULTIPLY, '*'),
            Token(TokenType.RIGHT_PAREN, ')'),
            Token(TokenType.INTEGER, 41),
            Token(TokenType.END_STATEMENT, 'End of Statement'),
            Token(TokenType.EOF, 'End of File')
        ]

        parser_response = Parser(tokens).parse()

        errors = parser_response.errors()

        assert errors[0] == 'Expect a open operator for TokenType.RIGHT_PAREN, Value: )'

    def test_parse_run_generates_correct_error_unopened_operators_right_brace(self):
        """
        Validates if parser if generating correct error to unopened operators
        """
        tokens = [
            Token(TokenType.INTEGER, 39),
            Token(TokenType.MULTIPLY, '*'),
            Token(TokenType.RIGHT_BRACE, '}'),
            Token(TokenType.INTEGER, 41),
            Token(TokenType.END_STATEMENT, 'End of Statement'),
            Token(TokenType.EOF, 'End of File')
        ]

        parser_response = Parser(tokens).parse()

        errors = parser_response.errors()

        assert errors[0] == 'Expect a open operator for TokenType.RIGHT_BRACE, Value: }'
