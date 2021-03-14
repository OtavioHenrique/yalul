from yalul.lex.token import Token
from yalul.lex.token_type import TokenType
from yalul.parser import Parser
from yalul.parsers.ast.nodes.statements.expressions.values.integer import Integer
from yalul.parsers.ast.nodes.statements.variable_declaration import VariableDeclaration


class TestVariableDeclarationStatements:
    """Test parser generating VariableDeclaration statements"""

    def test_parser_run_generates_correct_ast_variable_statements(self):
        """
        Validates if parser is generating a correct AST for variable declaration statements
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

        assert len(parser_response.errors()) == 0

        assert type(first_statement_ast) is VariableDeclaration
        assert first_statement_ast.name == "everything"

        assert type(first_statement_ast.initializer) is Integer
        assert first_statement_ast.initializer.value == 42
