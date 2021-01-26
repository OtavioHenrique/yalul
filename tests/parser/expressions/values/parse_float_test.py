from yalul.parser import Parser
from yalul.lex.token import Token
from yalul.lex.token_type import TokenType
from yalul.parsers.ast.nodes.statements.expressions.values.float import Float


class TestParseFloat:
    """Test parser generating single values float"""

    def test_parser_run_generates_correct_ast_single_value_float(self):
        """
        Validates if parser is generating a correct AST to a single value of type float
        """
        tokens = [
            Token(TokenType.FLOAT, "42.42"),
            Token(TokenType.END_STATEMENT, "End of Statement"),
            Token(TokenType.EOF, "End of File")
        ]

        ast = Parser(tokens).parse()

        node = ast[0]

        assert type(node) is Float
        assert node.value == "42.42"
