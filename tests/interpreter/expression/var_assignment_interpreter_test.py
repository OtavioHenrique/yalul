from yalul.interpreters.environment import Environment
from yalul.interpreters.expressions.var_assignment_interpreter import VarAssignmentInterpreter
from yalul.interpreters.interpreter_errors import InterpreterErrors


class TestVarAssignmentInterpreter:
    """Test var assignment expression interpreter"""

    def test_interpreting_var_assignment_without_errors(self):
        """
        Validates if VarAssignmentInterpreter is interpreting correctly
        """
        error = InterpreterErrors()
        env = Environment({}, {})

        env.add_variable('Name', 'Gabriela')

        interpreter = VarAssignmentInterpreter('Name', 'Otavio', env, error)

        response = interpreter.execute()

        assert response == 'Otavio'
        assert env.get_variable('Name') == 'Otavio'
        assert error.errors == []

    def test_interpreting_var_assignment_errors(self):
        """
        Validates if VarAssignmentInterpreter is generating errors when variable don't exists
        """
        error = InterpreterErrors()
        env = Environment({}, {})

        interpreter = VarAssignmentInterpreter('Name', 'Otavio', env, error)

        response = interpreter.execute()

        assert response is None
        assert error.errors == ['Interpreter Error: Can\'t assign value Otavio to variable named "Name" because it '
                                'doesn\'t exists']
