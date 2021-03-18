from yalul.lex.token import Token
from yalul.lex.token_type import TokenType
from yalul.parser import Parser
from yalul.parsers.ast.nodes.statements.expressions.grouping import Grouping
from yalul.parsers.ast.nodes.statements.expressions.binary import Binary
from yalul.parsers.ast.nodes.statements.expressions.var_assignment import VarAssignment
from yalul.parsers.ast.nodes.statements.if_statement import If


class TestIfStatements:
    """Test parser generating if statements"""

    def test_parser_run_generates_correct_ast_if_statements(self):
        """
        Validates if parser is generating a correct AST for if statements
        """
        tokens = [
            Token(TokenType.IF, 'if'),
            Token(TokenType.LEFT_PAREN, '('),
            Token(TokenType.INTEGER, '42'),
            Token(TokenType.GREATER, '>'),
            Token(TokenType.INTEGER, '1'),
            Token(TokenType.RIGHT_PAREN, ')'),
            Token(TokenType.LEFT_BRACE, '{'),
            Token(TokenType.IDENTIFIER, 'everything'),
            Token(TokenType.EQUAL, '='),
            Token(TokenType.INTEGER, '42'),
            Token(TokenType.END_STATEMENT, 'End of Statement'),
            Token(TokenType.INTEGER, '1'),
            Token(TokenType.SUM, '+'),
            Token(TokenType.INTEGER, '90'),
            Token(TokenType.END_STATEMENT, 'End of Statement'),
            Token(TokenType.RIGHT_BRACE, '}'),
            Token(TokenType.END_STATEMENT, 'End of Statement'),
            Token(TokenType.EOF, 'End of File')
        ]

        parser_response = Parser(tokens).parse()
        first_statement_ast = parser_response.ast.statements[0]

        assert type(first_statement_ast) is If
        assert type(first_statement_ast.condition) is Grouping
        assert type(first_statement_ast.condition.value) is Binary
        assert len(first_statement_ast.then_block.statements) == 2
        assert type(first_statement_ast.then_block.statements[0]) is VarAssignment
        assert type(first_statement_ast.then_block.statements[1]) is Binary
        assert first_statement_ast.else_block is None


class TestIfElseStatements:
    """Test parser generating else statements"""

    def test_parser_run_generates_correct_ast_if_else_statements(self):
        """
        Validates if parser is generating a correct AST for if else statements
        """
        tokens = [
            Token(TokenType.IF, 'if'),
            Token(TokenType.LEFT_PAREN, '('),
            Token(TokenType.INTEGER, '42'),
            Token(TokenType.GREATER, '>'),
            Token(TokenType.INTEGER, '1'),
            Token(TokenType.RIGHT_PAREN, ')'),
            Token(TokenType.LEFT_BRACE, '{'),
            Token(TokenType.IDENTIFIER, 'everything'),
            Token(TokenType.EQUAL, '='),
            Token(TokenType.INTEGER, '42'),
            Token(TokenType.END_STATEMENT, 'End of Statement'),
            Token(TokenType.INTEGER, '1'),
            Token(TokenType.SUM, '+'),
            Token(TokenType.INTEGER, '90'),
            Token(TokenType.END_STATEMENT, 'End of Statement'),
            Token(TokenType.RIGHT_BRACE, '}'),
            Token(TokenType.ELSE, 'else'),
            Token(TokenType.LEFT_BRACE, '{'),
            Token(TokenType.IDENTIFIER, 'everything'),
            Token(TokenType.EQUAL, '='),
            Token(TokenType.INTEGER, '42'),
            Token(TokenType.END_STATEMENT, 'End of Statement'),
            Token(TokenType.RIGHT_BRACE, '}'),
            Token(TokenType.END_STATEMENT, 'End of Statement'),
            Token(TokenType.EOF, 'End of File')
        ]

        parser_response = Parser(tokens).parse()
        first_statement_ast = parser_response.ast.statements[0]

        assert len(parser_response.errors()) == 0

        assert type(first_statement_ast) is If
        assert type(first_statement_ast.condition) is Grouping
        assert type(first_statement_ast.condition.value) is Binary
        assert len(first_statement_ast.then_block.statements) == 2
        assert type(first_statement_ast.then_block.statements[0]) is VarAssignment
        assert type(first_statement_ast.then_block.statements[1]) is Binary

        assert first_statement_ast.else_block is not None
        assert len(first_statement_ast.else_block.statements) == 1
        assert type(first_statement_ast.else_block.statements[0]) is VarAssignment
