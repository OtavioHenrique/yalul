class While:
    """
    Yalul's while statement
    """

    def __init__(self, condition, block):
        """
        Construct a new while statement object.

        :condition: while condition (grouping expression)
        :block: block statement
        """
        self.condition = condition
        self.block = block
