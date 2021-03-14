from yalul.lex.token_type import TokenType
from yalul.lex.token import Token as LexerToken
from yalul.parsers.parse_errors import ParseErrors
from yalul.parsers.parser_base import ParserBase
from yalul.parsers.token_counter import TokenCounter


class TestParserBase:
    """Test ParserBase"""

    def test_consume_when_current_token_eof(self):
        """
        Test consume method when current_token is EOF
        """
        tokens = [
            LexerToken(TokenType.EOF, 'End of File')
        ]

        parser = ParserBase(tokens, TokenCounter(0), ParseErrors([]), None)

        assert parser.consume(TokenType.INTEGER, 'dummy') is None

    def test_consume_when_current_token_is_expected(self):
        """
        Test consume method when current token is expected
        """
        expected_token = LexerToken(TokenType.INTEGER, 42)

        tokens = [expected_token]

        parser = ParserBase(tokens, TokenCounter(0), ParseErrors([]), None)

        assert parser.consume(TokenType.INTEGER, 'dummy') == expected_token

    def test_consume_when_current_token_is_different_expected(self):
        """
        Test consume method when current token is not expected
        """
        token = LexerToken(TokenType.INTEGER, 42)

        tokens = [token]

        parser = ParserBase(tokens, TokenCounter(0), ParseErrors([]), None)

        parser.consume(TokenType.STRING, 'dummy error')

        assert len(parser.errors.errors) == 1
        assert parser.errors.errors[0] == 'dummy error'

    def test_current_token(self):
        """
        Test current_token method
        """
        expected_token = LexerToken(TokenType.VARIABLE, 'Variable identifier')

        tokens = [
            expected_token,
            LexerToken(TokenType.INTEGER, 42),
            LexerToken(TokenType.END_STATEMENT, 'End of Statement'),
            LexerToken(TokenType.EOF, 'End of File')
        ]

        parser = ParserBase(tokens, TokenCounter(0), ParseErrors([]), None)

        assert parser.current_token() == expected_token

    def test_last_token(self):
        """
        Test last_token method
        """
        expected_token = LexerToken(TokenType.VARIABLE, 'Variable identifier')

        tokens = [
            expected_token,
            LexerToken(TokenType.INTEGER, 42),
            LexerToken(TokenType.END_STATEMENT, 'End of Statement'),
            LexerToken(TokenType.EOF, 'End of File')
        ]

        parser = ParserBase(tokens, TokenCounter(1), ParseErrors([]), None)

        assert parser.last_token() == expected_token
