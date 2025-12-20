from .base import SessionManager

class MessageManager:
    def __init__(self, session: SessionManager):
        self.session = session

    def get(self, chat_id: int):
        return self.session.get(chat_id, f"menu_{chat_id}")

    def set(self, chat_id: int, message_id: int):
        self.session.set(chat_id, f"menu_{chat_id}", message_id)

    def clear(self, chat_id: int):
        self.session.set(chat_id, f"menu_{chat_id}", None)
