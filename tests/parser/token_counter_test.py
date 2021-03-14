from yalul.parsers.token_counter import TokenCounter


class TestTokenCounter:
    """Test Token Counter"""

    def test_current(self):
        """
        Test current method
        """
        token_counter = TokenCounter(1)

        assert token_counter.current() == 1

    def test_increment(self):
        """
        Test increment method
        """

        token_counter = TokenCounter(0)
        token_counter.increment()

        assert token_counter.current() == 1
