class CommandRegistry:
    def __init__(self):
        self._commands = {}

    def register(self, name: str, handler):
        self._commands[name] = handler

    def get(self, name: str):
        return self._commands.get(name)
