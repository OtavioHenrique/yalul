from yalul.interpreters.environment import Environment
from yalul.interpreters.interpreter_errors import InterpreterErrors
from yalul.interpreters.print_interpreter import PrintInterpreter
from yalul.parsers.abstract_syntax_tree import AbstractSyntaxTree
from yalul.parsers.ast.nodes.statements.expressions.grouping import Grouping
from yalul.parsers.ast.nodes.statements.expressions.values.string import String
from yalul.parsers.ast.nodes.statements.print import Print


class TestPrintInterpreter:
    """Test print interpreter"""

    def test_interpreting_print_statements(self, capsys):
        """
        Validates if interpreter is interpreting variable print correctly
        """
        env = Environment()
        error = InterpreterErrors()
        ast = AbstractSyntaxTree([
            Print(Grouping(String('Gabriela')))
        ])

        PrintInterpreter(ast.statements[0], env, error).execute()

        captured = capsys.readouterr()

        assert captured.out == 'Gabriela\n'
