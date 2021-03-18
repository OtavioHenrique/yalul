from yalul.lex.token import Token
from yalul.lex.token_type import TokenType
from yalul.parser import Parser
from yalul.parsers.ast.nodes.statements.expressions.binary import Binary
from yalul.parsers.ast.nodes.statements.expressions.return_expression import Return
from yalul.parsers.ast.nodes.statements.func import Func


class TestFuncStatements:
    """Test parser generating func statements"""

    def test_parser_run_generates_correct_ast_func_statements(self):
        """
        Validates if parser is generating a correct AST for func statements
        """
        tokens = [
            Token(TokenType.FUNCTION, 'func'),
            Token(TokenType.IDENTIFIER, 'sum'),
            Token(TokenType.LEFT_PAREN, '('),
            Token(TokenType.IDENTIFIER, 'a'),
            Token(TokenType.IDENTIFIER, 'b'),
            Token(TokenType.RIGHT_PAREN, ')'),
            Token(TokenType.LEFT_BRACE, '{'),
            Token(TokenType.RETURN, 'return'),
            Token(TokenType.IDENTIFIER, 'a'),
            Token(TokenType.SUM, '+'),
            Token(TokenType.IDENTIFIER, 'b'),
            Token(TokenType.END_STATEMENT, 'End of Statement'),
            Token(TokenType.RIGHT_BRACE, '}'),
            Token(TokenType.END_STATEMENT, 'End of Statement'),
            Token(TokenType.EOF, 'End of File')
        ]

        parser_response = Parser(tokens).parse()
        first_statement_ast = parser_response.ast.statements[0]

        assert len(parser_response.errors()) == 0

        assert type(first_statement_ast) is Func
        assert first_statement_ast.identifier == 'sum'
        assert len(first_statement_ast.parameters) == 2
        assert len(first_statement_ast.block.statements) == 1
        assert type(first_statement_ast.block.statements[0]) is Return
        assert type(first_statement_ast.block.statements[0].value) is Binary
