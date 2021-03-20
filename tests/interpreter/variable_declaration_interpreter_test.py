from yalul.interpreters.environment import Environment
from yalul.interpreters.interpreter_errors import InterpreterErrors
from yalul.interpreters.variable_declaration import VariableDeclarationInterpreter
from yalul.parsers.abstract_syntax_tree import AbstractSyntaxTree
from yalul.parsers.ast.nodes.statements.expressions.values.string import String
from yalul.parsers.ast.nodes.statements.variable_declaration import VariableDeclaration


class TestVariableDeclarationInterpreter:
    """Test variable declaration interpreter"""

    def test_interpreting_variable_declaration_statements(self):
        """
        Validates if interpreter is interpreting variable declaration statements correctly
        """
        env = Environment()
        error = InterpreterErrors()
        ast = AbstractSyntaxTree([
            VariableDeclaration('name', String('Gabriela'))
        ])

        VariableDeclarationInterpreter(ast.statements[0], env, error).execute()

        assert env.get_variable('name') == 'Gabriela'
