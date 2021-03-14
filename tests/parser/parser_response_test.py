from yalul.parsers.parse_response import ParseResponse


class DummyErrors:
    def __init__(self, errors):
        self.errors = errors


class TestParserResponse:
    """Test Parser Response"""

    def test_errors(self):
        """
        Test errors method
        """
        errors = DummyErrors(['dummy'])
        parser_response = ParseResponse([], errors)

        assert parser_response.errors() == errors.errors
