from aiogram.types import Message

class CommandContext:
    def __init__(self, app, message: Message):
        self.app = app
        self.bot = app.bot
        self.message = message
        self.chat_id = message.chat.id
        self.user_id = message.from_user.id

    async def delete(self):
        try:
            await self.message.delete()
        except Exception:
            pass

    async def render(self, path: str):
        await self.app._render(self.chat_id, path, source="command")
