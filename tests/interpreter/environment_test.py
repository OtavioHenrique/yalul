from yalul.interpreters.environment import Environment


class TestEnvironment:
    """Test if environment is working correctly"""

    def test_environment_add_variable(self):
        """
        Validates if environment is adding new variables correctly
        """
        env = Environment()

        env.add_variable('name', 'Gabriela')

        assert env.environment_table['name'] == 'Gabriela'