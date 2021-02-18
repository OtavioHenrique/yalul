class Variable:
    """
    Yalul's variable statement
    """

    def __init__(self, name, initializer):
        """
        Construct a new Variable statement object.

        :name: variable identifier (name)
        :initializer: variable expression initializer
        """
        self.name = name
        self.initializer = initializer
