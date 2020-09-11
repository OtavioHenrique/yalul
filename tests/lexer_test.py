import pytest
from pathlib import Path
from yalul.lexer import Lexer
from yalul.lex.token_type import TokenType


@pytest.fixture(scope='function')
def open_file(request):
    return open(str(Path.cwd()) + "/tests/lex_examples/" + request.param)


class TestLexerInteger:
    """
    Test lexer for integers tokens
    """

    @pytest.mark.parametrize('open_file', ['integers_example.yalul'], indirect=['open_file'])
    def test_lexer_run(self, open_file):
        """
        Receives a source containing integers and lex it to integers tokens
        """
        lexer = Lexer(open_file)
        tokens = lexer.run()

        for token in tokens:
            assert token.type == TokenType.INTEGER


class TestLexerOperators:
    """
    Test lexer for operators tokens
    """
    @pytest.mark.parametrize('open_file', ['operators_example.yalul'], indirect=['open_file'])
    def test_lexer_run(self, open_file):
        """
        Receives a source containing operators and lex it to operator tokens
        """
        lexer = Lexer(open_file)
        tokens = lexer.run()

        expected_tokens = [TokenType.SUM, TokenType.MINUS, TokenType.MULTIPLY, TokenType.DIVISION]

        for index, token in enumerate(tokens):
            assert token.type == expected_tokens[index]
