from yalul.parser import Parser
from yalul.parsers.ast.nodes.statements.expressions.binary import Binary
from yalul.lex.token import Token
from yalul.lex.token_type import TokenType
from yalul.parsers.ast.nodes.statements.expressions.return_expression import Return


class TestParserReturnExpressions:
    """Test parser generating return expressions"""

    def test_parser_run_generates_correct_ast_with_return_expressions(self):
        """
        Validates if parser is generating a correct AST for return expressions
        """
        tokens = [
            Token(TokenType.RETURN, 'return'),
            Token(TokenType.INTEGER, 20),
            Token(TokenType.SUM, "+"),
            Token(TokenType.INTEGER, 42),
            Token(TokenType.END_STATEMENT, "End of Statement"),
            Token(TokenType.EOF, "End of File")
        ]

        parser_response = Parser(tokens).parse()

        assert len(parser_response.errors()) == 0

        first_statement_ast = parser_response.ast.statements[0]

        assert type(first_statement_ast) is Return
        assert type(first_statement_ast.value) is Binary
