class NavigationStack:
    def __init__(self):
        self.stack = {}

    def push(self, chat_id: int, path: str):
        self.stack.setdefault(chat_id, [])
        if not self.stack[chat_id] or self.stack[chat_id][-1] != path:
            self.stack[chat_id].append(path)

    def back(self, chat_id: int):
        if chat_id not in self.stack or len(self.stack[chat_id]) <= 1:
            return "/"
        self.stack[chat_id].pop()
        return self.stack[chat_id][-1]

    def current(self, chat_id: int):
        if chat_id not in self.stack or not self.stack[chat_id]:
            return "/"
        return self.stack[chat_id][-1]
