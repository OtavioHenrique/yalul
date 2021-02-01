from yalul.parser import Parser
from yalul.parsers.ast.nodes.statements.expressions.binary import Binary
from yalul.lex.token import Token
from yalul.lex.token_type import TokenType
from yalul.parsers.ast.nodes.statements.expressions.grouping import Grouping
from yalul.parsers.ast.nodes.statements.expressions.values.integer import Integer


class TestParserGroupingExpressions:
    """Test parser generating grouping expressions"""

    def test_parser_run_generates_correct_ast_with_grouping_expressions(self):
        """
        Validates if parser is generating a correct AST for grouping expressions
        """
        tokens = [
            Token(TokenType.INTEGER, 39),
            Token(TokenType.MULTIPLY, "*"),
            Token(TokenType.LEFT_PAREN, "Left Paren"),
            Token(TokenType.INTEGER, 20),
            Token(TokenType.SUM, "+"),
            Token(TokenType.INTEGER, 42),
            Token(TokenType.RIGHT_PAREN, "Right Paren"),
            Token(TokenType.END_STATEMENT, "End of Statement"),
            Token(TokenType.EOF, "End of File")
        ]

        ast = Parser(tokens).parse()

        first_statement_ast = ast[0]

        assert type(first_statement_ast) is Binary
        assert first_statement_ast.operator.type is TokenType.MULTIPLY

        assert type(first_statement_ast.left) is Integer
        assert first_statement_ast.left.value == 39

        grouping = first_statement_ast.right

        assert type(grouping) is Grouping
        assert type(grouping.value) is Binary

        assert grouping.value.operator.type is TokenType.SUM
        assert grouping.value.left.value == 20
        assert grouping.value.right.value == 42
