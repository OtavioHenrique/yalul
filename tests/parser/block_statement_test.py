from yalul.lex.token import Token
from yalul.lex.token_type import TokenType
from yalul.parser import Parser
from yalul.parsers.ast.nodes.statements.block import Block


class TestBlockStatements:
    """Test parser generating block statements"""

    def test_parser_run_generates_correct_ast_block_statements(self):
        """
        Validates if parser is generating a correct AST for block statements
        """
        tokens = [
            Token(TokenType.LEFT_BRACE, 'Brace'),
            Token(TokenType.INTEGER, '42'),
            Token(TokenType.SUM, '+'),
            Token(TokenType.INTEGER, '1'),
            Token(TokenType.RIGHT_BRACE, 'Brace'),
            Token(TokenType.END_STATEMENT, 'End of Statement'),
            Token(TokenType.EOF, 'End of File')
        ]

        parser_response = Parser(tokens).parse()
        first_statement_ast = parser_response.asts[0]

        assert type(first_statement_ast) is Block
