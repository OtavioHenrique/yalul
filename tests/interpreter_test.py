from yalul.interpreter import Interpreter
from yalul.parsers.abstract_syntax_tree import AbstractSyntaxTree
from yalul.parsers.ast.nodes.statements.expressions.values.integer import Integer


class TestInterpreter:
    """Test Interpreter"""

    def test_interpreter_running_multiple_statements(self, capsys):
        """Test interpreter interpreting multiple statements"""
        ast = AbstractSyntaxTree([
            Integer(1),
            Integer(41)
        ])

        interpreter = Interpreter(ast)
        interpreter.run()
        captured = capsys.readouterr()

        assert captured.out == '1\n41\n'
