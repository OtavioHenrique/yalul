class If:
    """
    Yalul's if statement
    """

    def __init__(self, condition, then_block, else_block):
        """
        Construct a new if statement object.

        :condition: if condition (grouping expression)
        :then_block: then block statement
        :else_block: else block statement
        """
        self.condition = condition
        self.then_block = then_block
        self.else_block = else_block
