from yalul.interpreters.expressions.binary import BinaryInterpreter
from yalul.interpreters.interpreter_errors import InterpreterErrors
from yalul.lex.token_type import TokenType


class TestBinaryInterpreter:
    """Test binary expression interpreter"""

    def test_interpreting_binary_sum_operation_without_errors(self):
        """
        Validates if BinaryInterpreter is interpreting sum operations correctly
        """
        error = InterpreterErrors()
        interpreter = BinaryInterpreter(TokenType.SUM, 41, 1, error)

        response = interpreter.execute()

        assert response == 42
        assert error.errors == []

    def test_interpreting_binary_multiply_operation_without_errors(self):
        """
        Validates if BinaryInterpreter is interpreting multiply operations correctly
        """
        error = InterpreterErrors()
        interpreter = BinaryInterpreter(TokenType.MULTIPLY, 42, 1, error)

        response = interpreter.execute()

        assert response == 42
        assert error.errors == []

    def test_interpreting_binary_division_operation_without_errors(self):
        """
        Validates if BinaryInterpreter is interpreting division operations correctly
        """
        error = InterpreterErrors()
        interpreter = BinaryInterpreter(TokenType.DIVISION, 42, 2, error)

        response = interpreter.execute()

        assert response == 21
        assert error.errors == []

    def test_interpreting_binary_minus_operation_without_errors(self):
        """
        Validates if BinaryInterpreter is interpreting minus operations correctly
        """
        error = InterpreterErrors()
        interpreter = BinaryInterpreter(TokenType.MINUS, 42, 1, error)

        response = interpreter.execute()

        assert response == 41
        assert error.errors == []

    def test_interpreting_binary_great_operation_without_errors(self):
        """
        Validates if BinaryInterpreter is interpreting greater operations correctly
        """

        error = InterpreterErrors()
        interpreter = BinaryInterpreter(TokenType.GREATER, 42, 1, error)

        response = interpreter.execute()

        assert bool(response) is True
        assert error.errors == []

        second_interpreter = BinaryInterpreter(TokenType.GREATER, 1, 42, error)

        second_response = second_interpreter.execute()

        assert bool(second_response) is False
        assert error.errors == []

    def test_interpreting_binary_less_operation_without_errors(self):
        """
        Validates if BinaryInterpreter is interpreting less operations correctly
        """

        error = InterpreterErrors()
        interpreter = BinaryInterpreter(TokenType.LESS, 42, 1, error)

        response = interpreter.execute()

        assert bool(response) is False
        assert error.errors == []

        second_interpreter = BinaryInterpreter(TokenType.LESS, 1, 42, error)

        second_response = second_interpreter.execute()

        assert bool(second_response) is True
        assert error.errors == []

    def test_interpreting_binary_equal_equal_operation_without_errors(self):
        """
        Validates if BinaryInterpreter is interpreting equal operations correctly
        """

        error = InterpreterErrors()
        interpreter = BinaryInterpreter(TokenType.EQUAL_EQUAL, 42, 42, error)

        response = interpreter.execute()

        assert bool(response) is True
        assert error.errors == []

        second_interpreter = BinaryInterpreter(TokenType.EQUAL_EQUAL, 1, 42, error)

        second_response = second_interpreter.execute()

        assert bool(second_response) is False
        assert error.errors == []

    def test_interpreting_binary_less_equal_operation_without_errors(self):
        """
        Validates if BinaryInterpreter is interpreting less equal operations correctly
        """

        error = InterpreterErrors()
        interpreter = BinaryInterpreter(TokenType.LESS_EQUAL, 1, 42, error)

        response = interpreter.execute()

        assert bool(response) is True
        assert error.errors == []

        second_interpreter = BinaryInterpreter(TokenType.LESS_EQUAL, 42, 42, error)

        second_response = second_interpreter.execute()

        assert bool(second_response) is True
        assert error.errors == []

    def test_interpreting_binary_greater_equal_operation_without_errors(self):
        """
        Validates if BinaryInterpreter is interpreting greater equal operations correctly
        """

        error = InterpreterErrors()
        interpreter = BinaryInterpreter(TokenType.GREATER_EQUAL, 42, 1, error)

        response = interpreter.execute()

        assert bool(response) is True
        assert error.errors == []

        second_interpreter = BinaryInterpreter(TokenType.GREATER_EQUAL, 42, 42, error)

        second_response = second_interpreter.execute()

        assert bool(second_response) is True
        assert error.errors == []

    def test_interpreting_binary_generating_errors_for_type_error(self):
        """
        Validates if BinaryInterpreter is generating errors for TypeError
        """
        error = InterpreterErrors()
        interpreter = BinaryInterpreter(TokenType.MINUS, 42, 'everything', error)

        response = interpreter.execute()

        assert response is None
        assert error.errors == ['Interpreter Error: Cannot execute BinaryOperation of operator TokenType.MINUS '
                                'between values 42 and everything']
