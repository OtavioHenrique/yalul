from yalul.interpreters.environment import Environment
from yalul.parsers.ast.nodes.statements.expressions.values.null import Null


class TestEnvironment:
    """Test if environment is working correctly"""

    def test_environment_add_variable(self):
        """
        Validates if environment is adding new variables correctly
        """
        env = Environment({}, {})

        env.add_variable('name', 'Gabriela')

        assert env.variables_table()['name'] == 'Gabriela'

    def test_show_variable_exists_when_identifier_exists(self):
        """
        Validates if method variable exists is working when given identifier exists
        """
        env = Environment({}, {})

        env.add_variable('name', 'Gabriela')

        assert env.variable_exists('name') is True

    def test_show_variable_exists_when_identifier_dont_exists(self):
        """
        Validates if method variable exists is working when given identifier dont exists
        """
        env = Environment({}, {})

        assert env.variable_exists('name') is False

    def test_show_get_variable_when_it_exists(self):
        """
        Validates if method get_variable is geting variable when it exists
        """
        env = Environment({}, {})

        env.add_variable('name', 'Gabriela')

        assert env.get_variable('name') == 'Gabriela'

    def test_show_get_variable_when_it_dont_exists(self):
        """
        Validates if method get_variable is returning null when given identifier dont exists
        """
        env = Environment({}, {})

        assert type(env.get_variable('name')) == Null

    def test_environment_add_func(self):
        """
        Validates if environment is adding new variables correctly
        """
        env = Environment({}, {})

        env.add_function('identifier', 'parameters', 'block')

        func = env.get_variable('identifier')

        assert func['name'] == 'identifier'
        assert func['parameters'] == 'parameters'
        assert func['block'] == 'block'

    def test_show_get_variable_when_it_exists(self):
        """
        Validates if method get_variable is geting variable when it exists
        """
        env = Environment({}, {})

        env.add_variable('name', 'Gabriela')

        assert env.get_variable('name') == 'Gabriela'

    def test_show_get_variable_when_it_dont_exists(self):
        """
        Validates if method get_variable is returning null when given identifier dont exists
        """
        env = Environment({}, {})

        assert type(env.get_variable('name')) == Null