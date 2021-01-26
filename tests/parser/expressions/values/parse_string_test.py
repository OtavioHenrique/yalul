from yalul.parser import Parser
from yalul.lex.token import Token
from yalul.lex.token_type import TokenType
from yalul.parsers.ast.nodes.statements.expressions.values.string import String


class TestParseString:
    """Test parser generating single values string"""

    def test_parser_run_generates_correct_ast_single_value_string(self):
        """
        Validates if parser is generating a correct AST to a single value of type string
        """
        tokens = [
            Token(TokenType.STRING, "Ola"),
            Token(TokenType.END_STATEMENT, "End of Statement"),
            Token(TokenType.EOF, "End of File")
        ]

        ast = Parser(tokens).parse()

        node = ast[0]

        assert type(node) is String
        assert node.value == "Ola"
