from yalul.lex.token_type import TokenType
from yalul.parser import Parser
from yalul.lex.token import Token
from yalul.parsers.ast.nodes.statements.expressions.variable import Variable


class TestParserVariablesExpressions:
    """Test parser generating multiple statements"""

    def test_parser_run_generates_correct_ast_with_multiple_statements(self):
        """
        Validates if parser is generating a correct AST for multiple statements
        """
        tokens = [
            Token(TokenType.IDENTIFIER, "everything"),
            Token(TokenType.END_STATEMENT, "End of Statement"),
            Token(TokenType.EOF, "End of File")
        ]

        parser_response = Parser(tokens).parse()

        first_statement_ast = parser_response.asts[0]

        assert type(first_statement_ast) is Variable
        assert first_statement_ast.value == "everything"
