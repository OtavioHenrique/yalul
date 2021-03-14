from yalul.parser import Parser
from yalul.lex.token import Token
from yalul.lex.token_type import TokenType
from yalul.parsers.ast.nodes.statements.expressions.values.integer import Integer


class TestParseInteger:
    """Test parser generating single values integer"""

    def test_parser_run_generates_correct_ast_single_value_integer(self):
        """
        Validates if parser is generating a correct AST to a single value of type integer
        """
        tokens = [
            Token(TokenType.INTEGER, "42"),
            Token(TokenType.END_STATEMENT, "End of Statement"),
            Token(TokenType.EOF, "End of File")
        ]

        parser_response = Parser(tokens).parse()
        assert len(parser_response.errors()) == 0

        node = parser_response.asts[0]

        assert type(node) is Integer
        assert node.value == "42"
