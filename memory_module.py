class MemoryModule:
    def __init__(self):
        self.history = []

    def add_message(self, message):
        self.history.append(message)
