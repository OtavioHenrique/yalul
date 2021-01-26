from yalul.parser import Parser
from yalul.lex.token import Token
from yalul.lex.token_type import TokenType
from yalul.parsers.ast.nodes.statements.expressions.values.null import Null


class TestParseNull:
    """Test parser generating single values null"""

    def test_parser_run_generates_correct_ast_single_value_null(self):
        """
        Validates if parser is generating a correct AST to a single value of type null
        """
        tokens = [
            Token(TokenType.NULL, "null"),
            Token(TokenType.END_STATEMENT, "End of Statement"),
            Token(TokenType.EOF, "End of File")
        ]

        ast = Parser(tokens).parse()

        node = ast[0]

        assert type(node) is Null
        assert node.value == "null"
