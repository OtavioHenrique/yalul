class Token:
    def __init__(self, type_type, value):
        self.type = type_type
        self.value = value

    def __str__(self):
        return "%s, Value: %s" % (self.type, self.value)
