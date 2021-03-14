from yalul.parsers.parse_errors import ParseErrors


class TestParserError:
    """Test Parser Error"""

    def test_add_errors(self):
        """
        Test add_errors method
        """
        parser_errors = ParseErrors([])

        assert parser_errors.errors == []

        parser_errors.add_error('dummy')

        assert parser_errors.errors == ['dummy']
