from yalul.interpreters.expression import ExpressionInterpreter
from yalul.interpreters.interpreter_errors import InterpreterErrors
from yalul.lex.token import Token
from yalul.lex.token_type import TokenType
from yalul.parsers.abstract_syntax_tree import AbstractSyntaxTree
from yalul.parsers.ast.nodes.statements.expressions.binary import Binary
from yalul.parsers.ast.nodes.statements.expressions.values.integer import Integer


class TestExpressionInterpreter:
    """Test expression interpreter"""

    def test_interpreting_value_expressions(self):
        """
        Validates if interpreter is interpreting value expressions correctly
        """
        error = InterpreterErrors()
        ast = AbstractSyntaxTree([
            Integer(1)
        ])

        response = ExpressionInterpreter.execute(ast.statements[0], error)

        assert response == 1
        assert error.errors == []

    def test_interpreting_binary_operation_expression(self):
        """
        Validates if interpreter is interpreting binary expressions correctly
        """
        error = InterpreterErrors()
        ast = AbstractSyntaxTree([
            Binary(Integer(41), Token(TokenType.SUM, "operator"), Integer(1))
        ])

        response = ExpressionInterpreter.execute(ast.statements[0], error)

        assert response == 42
        assert error.errors == []

