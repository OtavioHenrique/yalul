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

        for token in tokens[:-2]:
            assert token.type == TokenType.INTEGER

        assert tokens[-2].type == TokenType.END_STATEMENT
        assert tokens[-1].type == TokenType.EOF


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

        expected_tokens = [
            TokenType.SUM,
            TokenType.MINUS,
            TokenType.MULTIPLY,
            TokenType.DIVISION,
            TokenType.END_STATEMENT,
            TokenType.EOF
        ]

        for index, token in enumerate(tokens):
            assert token.type == expected_tokens[index]


class TestLexerComparisonOperators:
    """
    Test lexer for comparison operators tokens
    """

    @pytest.mark.parametrize('open_file', ['comparison_operators_example.yalul'], indirect=['open_file'])
    def test_lexer_run_comparison(self, open_file):
        """
        Receives a source containing comparison operators and lex it to operator tokens
        """
        lexer = Lexer(open_file)
        tokens = lexer.run()

        expected_tokens = [
            TokenType.GREATER,
            TokenType.LESS,
            TokenType.EQUAL,
            TokenType.BANG_EQUAL,
            TokenType.BANG,
            TokenType.LESS_EQUAL,
            TokenType.GREATER_EQUAL,
            TokenType.EQUAL_EQUAL,
            TokenType.END_STATEMENT,
            TokenType.EOF
        ]

        for index, token in enumerate(tokens):
            assert token.type == expected_tokens[index]


class TestLexerErrorToken:
    """
    Test lexer for error tokens
    """

    @pytest.mark.parametrize('open_file', ['unexpected_tokens_example.yalul'], indirect=['open_file'])
    def test_lexer_run_error_tokens(self, open_file):
        """
        Receives a source containing invalid tokens and lex it to error tokens
        """
        lexer = Lexer(open_file)
        tokens = lexer.run()

        expected_tokens = [
            TokenType.ERROR,
            TokenType.ERROR,
            TokenType.END_STATEMENT,
            TokenType.EOF
        ]

        for index, token in enumerate(tokens):
            assert token.type == expected_tokens[index]


class TestLexerSeparateStatements:
    """
    Test lexer separating statements
    """

    @pytest.mark.parametrize('open_file', ['separate_statements_example.yalul'], indirect=['open_file'])
    def test_lexer_run_separate_statements(self, open_file):
        """
        Receives a source containing expression and a separate statement
        """
        lexer = Lexer(open_file)

        tokens = lexer.run()

        expected_tokens = [
            TokenType.INTEGER,
            TokenType.SUM,
            TokenType.INTEGER,
            TokenType.DIVISION,
            TokenType.INTEGER,
            TokenType.END_STATEMENT,
            TokenType.INTEGER,
            TokenType.SUM,
            TokenType.INTEGER,
            TokenType.END_STATEMENT,
            TokenType.EOF
        ]

        for index, token in enumerate(tokens):
            assert token.type == expected_tokens[index]


class TestLexerVariableCreationStatements:
    """
    Test lexer lexing variable creation
    """

    @pytest.mark.parametrize('open_file', ['keywords/variable_example.yalul'], indirect=['open_file'])
    def test_lexer_run_variable_creation(self, open_file):
        """
        Receives a source containing variable creation
        """
        lexer = Lexer(open_file)

        tokens = lexer.run()

        expected_tokens = [
            TokenType.VARIABLE,
            TokenType.IDENTIFIER,
            TokenType.EQUAL,
            TokenType.STRING,
            TokenType.END_STATEMENT,
            TokenType.EOF
        ]

        for index, token in enumerate(tokens):
            assert token.type == expected_tokens[index]


class TestLexerBlocksStatements:
    """
    Test lexer lexing blocks
    """

    @pytest.mark.parametrize('open_file', ['block_example.yalul'], indirect=['open_file'])
    def test_lexer_run_block(self, open_file):
        """
        Receives a source containing a block
        """
        lexer = Lexer(open_file)

        tokens = lexer.run()

        expected_tokens = [
            TokenType.LEFT_BRACE,
            TokenType.INTEGER,
            TokenType.SUM,
            TokenType.INTEGER,
            TokenType.END_STATEMENT,
            TokenType.RIGHT_BRACE,
            TokenType.END_STATEMENT,
            TokenType.EOF
        ]

        for index, token in enumerate(tokens):
            assert token.type == expected_tokens[index]


class TestLexerIfStatements:
    """
    Test lexer lexing ifs
    """

    @pytest.mark.parametrize('open_file', ['keywords/if_example.yalul'], indirect=['open_file'])
    def test_lexer_run_block(self, open_file):
        """
        Receives a source containing a if
        """
        lexer = Lexer(open_file)

        tokens = lexer.run()

        expected_tokens = [
            TokenType.IF,
            TokenType.LEFT_PAREN,
            TokenType.INTEGER,
            TokenType.LESS,
            TokenType.INTEGER,
            TokenType.RIGHT_PAREN,
            TokenType.LEFT_BRACE,
            TokenType.IDENTIFIER,
            TokenType.EQUAL,
            TokenType.INTEGER,
            TokenType.END_STATEMENT,
            TokenType.RIGHT_BRACE,
            TokenType.END_STATEMENT,
            TokenType.EOF
        ]

        for index, token in enumerate(tokens):
            assert token.type == expected_tokens[index]
