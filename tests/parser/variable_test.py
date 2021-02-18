from yalul.lex.token import Token
from yalul.lex.token_type import TokenType
from yalul.parser import Parser
from yalul.parsers.ast.nodes.statements.expressions.values.integer import Integer
from yalul.parsers.ast.nodes.statements.variable import Variable


class TestVariableStatements:
    """Test parser generating variable statements"""

    def test_parser_run_generates_correct_ast_variable_statements(self):
        """
        Validates if parser is generating a correct AST for variable statements
        """
        tokens = [
            Token(TokenType.VARIABLE, "Variable identifier"),
            Token(TokenType.IDENTIFIER, "everything"),
            Token(TokenType.EQUAL, "="),
            Token(TokenType.INTEGER, 42),
            Token(TokenType.END_STATEMENT, "End of Statement"),
            Token(TokenType.EOF, "End of File")
        ]

        parser_response = Parser(tokens).parse()
        first_statement_ast = parser_response.asts[0]

        assert type(first_statement_ast) is Variable
        assert first_statement_ast.name is "everything"

        assert type(first_statement_ast.initializer) is Integer
        assert first_statement_ast.initializer.value == 42
