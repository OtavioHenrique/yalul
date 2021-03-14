from yalul.lex.token import Token
from yalul.lex.token_type import TokenType
from yalul.parser import Parser
from yalul.parsers.ast.nodes.statements.expressions.grouping import Grouping
from yalul.parsers.ast.nodes.statements.expressions.binary import Binary
from yalul.parsers.ast.nodes.statements.expressions.var_assignment import VarAssignment
from yalul.parsers.ast.nodes.statements.while_statement import While


class TestWhileStatements:
    """Test parser generating while statements"""

    def test_parser_run_generates_correct_ast_while_statements(self):
        """
        Validates if parser is generating a correct AST for while statements
        """
        tokens = [
            Token(TokenType.WHILE, 'while'),
            Token(TokenType.LEFT_PAREN, '('),
            Token(TokenType.IDENTIFIER, 'everything'),
            Token(TokenType.LESS, '<'),
            Token(TokenType.INTEGER, '42'),
            Token(TokenType.RIGHT_PAREN, ')'),
            Token(TokenType.LEFT_BRACE, '{'),
            Token(TokenType.IDENTIFIER, 'everything'),
            Token(TokenType.EQUAL, '='),
            Token(TokenType.IDENTIFIER, 'everything'),
            Token(TokenType.SUM, '+'),
            Token(TokenType.INTEGER, '1'),
            Token(TokenType.END_STATEMENT, 'End of Statement'),
            Token(TokenType.RIGHT_BRACE, '}'),
            Token(TokenType.END_STATEMENT, 'End of Statement'),
            Token(TokenType.EOF, 'End of File')
        ]

        parser_response = Parser(tokens).parse()
        first_statement_ast = parser_response.asts[0]

        assert len(parser_response.errors()) == 0

        assert type(first_statement_ast) is While
        assert type(first_statement_ast.condition) is Grouping
        assert type(first_statement_ast.condition.value) is Binary
        assert len(first_statement_ast.block.statements) == 1
        assert type(first_statement_ast.block.statements[0]) is VarAssignment
