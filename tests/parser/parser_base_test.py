from yalul.lex.token_type import TokenType
from yalul.lex.token import Token as LexerToken
from yalul.parsers.parse_errors import ParseErrors
from yalul.parsers.parser_base import ParserBase
from yalul.parsers.token_counter import TokenCounter


class TestParserBase:
    """Test ParserBase"""

    def test_current_token(self):
        """
        Test current_token method
        """
        expected_token = LexerToken(TokenType.VARIABLE, "Variable identifier")

        tokens = [
            expected_token,
            LexerToken(TokenType.INTEGER, 42),
            LexerToken(TokenType.END_STATEMENT, "End of Statement"),
            LexerToken(TokenType.EOF, "End of File")
        ]

        parser = ParserBase(tokens, TokenCounter(0), ParseErrors([]), None)

        assert parser.current_token() == expected_token
