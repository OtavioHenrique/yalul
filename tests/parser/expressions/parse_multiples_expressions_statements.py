from yalul.parser import Parser
from yalul.parsers.ast.nodes.statements.expressions.binary import Binary
from yalul.parsers.ast.nodes.statements.expressions.value import Value
from yalul.lex.token import Token
from yalul.lex.token_type import TokenType


class TestParserMultipleStatements:
    """Test parser generating multiple statements"""

    def test_parser_run_generates_correct_ast_with_multiple_statements(self):
        """
        Validates if parser is generating a correct AST for multiple statements
        """
        tokens = [
            Token(TokenType.INTEGER, 39),
            Token(TokenType.MULTIPLY, "*"),
            Token(TokenType.INTEGER, 2),
            Token(TokenType.END_STATEMENT, "End of Statement"),
            Token(TokenType.INTEGER, 20),
            Token(TokenType.SUM, "+"),
            Token(TokenType.INTEGER, 42),
            Token(TokenType.END_STATEMENT, "End of Statement"),
            Token(TokenType.EOF, "End of File")
        ]

        ast = Parser(tokens).parse()

        first_statement_ast = ast[0]

        assert type(first_statement_ast) is Binary
        assert first_statement_ast.operator.type is TokenType.MULTIPLY

        assert type(first_statement_ast.left) is Value
        assert first_statement_ast.left.value == 39

        assert type(first_statement_ast.right) is Value
        assert first_statement_ast.right.value == 2

        second_statement_ast = ast[1]

        assert type(second_statement_ast) is Binary
        assert second_statement_ast.operator.type is TokenType.SUM

        assert type(second_statement_ast.left) is Value
        assert second_statement_ast.left.value == 20

        assert type(second_statement_ast.right) is Value
        assert second_statement_ast.right.value == 42
