from yalul.parser import Parser
from yalul.lex.token import Token
from yalul.lex.token_type import TokenType
from yalul.parsers.ast.nodes.statements.expressions.values.boolean import Boolean


class TestParseBoolean:
    """Test parser generating single values Boolean"""

    def test_parser_run_generates_correct_ast_single_value_boolean_true(self):
        """
        Validates if parser is generating a correct AST to a single value of type true boolean
        """
        tokens = [
            Token(TokenType.TRUE, "true"),
            Token(TokenType.END_STATEMENT, "End of Statement"),
            Token(TokenType.EOF, "End of File")
        ]

        ast = Parser(tokens).parse()

        node = ast[0]

        assert type(node) is Boolean
        assert node.value == "true"

    def test_parser_run_generates_correct_ast_single_value_boolean_false(self):
        """
        Validates if parser is generating a correct AST to a single value of type false boolean
        """
        tokens = [
            Token(TokenType.FALSE, "false"),
            Token(TokenType.END_STATEMENT, "End of Statement"),
            Token(TokenType.EOF, "End of File")
        ]

        ast = Parser(tokens).parse()

        node = ast[0]

        assert type(node) is Boolean
        assert node.value == "false"
