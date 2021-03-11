class Func:
    """
    Yalul's func statement
    """

    def __init__(self, identifier, parameters, block):
        """
        Construct a new func statement object.

        :identifier: func identifier
        :parameters: array of function parameters
        :block: block statement
        """
        self.identifier = identifier
        self.parameters = parameters
        self.block = block
