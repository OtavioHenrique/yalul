from yalul.interpreters.environment import Environment
from yalul.interpreters.expressions.variable_interpreter import VariableInterpreter
from yalul.interpreters.interpreter_errors import InterpreterErrors


class TestVariableInterpreter:
    """Test VariableInterpreter expression interpreter"""

    def test_interpreting_var_assignment_without_errors(self):
        """
        Validates if VariableInterpreter is interpreting correctly
        """
        error = InterpreterErrors()
        env = Environment({})

        env.add_variable('Name', 'Gabriela')

        interpreter = VariableInterpreter('Name', env, error)

        response = interpreter.execute()

        assert response == 'Gabriela'
        assert error.errors == []

    def test_interpreting_var_assignment_errors(self):
        """
        Validates if VariableInterpreter is generating errors when variable don't exists
        """
        error = InterpreterErrors()
        env = Environment({})

        interpreter = VariableInterpreter('Name', env, error)

        response = interpreter.execute()

        assert response is None
        assert error.errors == ['Interpreter Error: Variable "Name" not initialized']
