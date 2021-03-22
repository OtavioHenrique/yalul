from yalul.lex.token import Token
from yalul.lex.token_type import TokenType
from yalul.parser import Parser
from yalul.parsers.ast.nodes.statements.expressions.grouping import Grouping
from yalul.parsers.ast.nodes.statements.expressions.values.string import String
from yalul.parsers.ast.nodes.statements.print import Print


class TestPrintStatements:
    """Test parser generating print statements"""

    def test_parser_run_generates_correct_ast_print_statements(self):
        """
        Validates if parser is generating a correct AST for print statements
        """
        tokens = [
            Token(TokenType.PRINT, 'print'),
            Token(TokenType.LEFT_PAREN, '('),
            Token(TokenType.STRING, 'Gabriela'),
            Token(TokenType.RIGHT_PAREN, ')'),
            Token(TokenType.END_STATEMENT, 'End of Statement'),
            Token(TokenType.EOF, 'End of File')
        ]

        parser_response = Parser(tokens).parse()
        first_statement_ast = parser_response.ast.statements[0]

        assert len(parser_response.errors()) == 0

        assert type(first_statement_ast) is Print
        assert type(first_statement_ast.value) is Grouping
        assert type(first_statement_ast.value.value) is String
