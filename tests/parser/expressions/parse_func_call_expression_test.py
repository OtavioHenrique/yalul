from yalul.parser import Parser
from yalul.parsers.ast.nodes.statements.expressions.binary import Binary
from yalul.lex.token import Token
from yalul.lex.token_type import TokenType
from yalul.parsers.ast.nodes.statements.expressions.func_call import FuncCall
from yalul.parsers.ast.nodes.statements.expressions.grouping import Grouping
from yalul.parsers.ast.nodes.statements.expressions.values.integer import Integer
from yalul.parsers.ast.nodes.statements.expressions.variable import Variable


class TestFuncCallExpressions:
    """Test parser generating function call expressions"""

    def test_parser_run_generates_correct_ast_with_func_call_expressions(self):
        """
        Validates if parser is generating a correct AST for function calls
        """
        tokens = [
            Token(TokenType.IDENTIFIER, 'sum'),
            Token(TokenType.LEFT_PAREN, "Left Paren"),
            Token(TokenType.INTEGER, 20),
            Token(TokenType.INTEGER, 42),
            Token(TokenType.RIGHT_PAREN, "Right Paren"),
            Token(TokenType.END_STATEMENT, "End of Statement"),
            Token(TokenType.EOF, "End of File")
        ]

        parser_response = Parser(tokens).parse()

        assert len(parser_response.errors()) == 0

        first_statement_ast = parser_response.asts[0]

        assert type(first_statement_ast) is FuncCall
        assert type(first_statement_ast.callee) is Variable
        assert len(first_statement_ast.arguments) == 2
        assert first_statement_ast.arguments[0].value == 20
        assert first_statement_ast.arguments[1].value == 42
