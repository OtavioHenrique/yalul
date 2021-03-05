from yalul.lex.token import Token
from yalul.lex.token_type import TokenType
from yalul.parser import Parser
from yalul.parsers.ast.nodes.statements.expressions.var_assignment import VarAssignment


class TestParserVarAssignmentExpression:
    """Test parser parsing var assignment expression"""

    def test_parser_run_generates_correct_ast_with_var_assignment(self):
        """
        Validates if parser is generating a correct AST for var assignment
        """
        tokens = [
            Token(TokenType.IDENTIFIER, "everything"),
            Token(TokenType.EQUAL, "="),
            Token(TokenType.INTEGER, 42),
            Token(TokenType.END_STATEMENT, "End of Statement"),
            Token(TokenType.EOF, "End of File")
        ]

        parser_response = Parser(tokens).parse()

        first_statement_ast = parser_response.asts[0]

        assert type(first_statement_ast) is VarAssignment
        assert first_statement_ast.identifier == 'everything'
        assert first_statement_ast.value.value == 42
