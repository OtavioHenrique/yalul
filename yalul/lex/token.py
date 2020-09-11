class Token:
    """
    A lex Token of the yalul language
    """
    def __init__(self, type, value):
        """
        Construct a new Token object.

        :params type: Type of the token, this type must be a TokenType
        :param value: The literal value of the token
        :return: returns nothing
        """
        self.type = type
        self.value = value

    def __str__(self):
        return "%s, Value: %s" % (self.type, self.value)
