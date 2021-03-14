class TokenCounter:
    def __init__(self, current):
        self.current_token = current

    def current(self):
        return self.current_token

    def increment(self):
        self.current_token += 1
        return self.current_token
