from aiogram.types import InlineKeyboardButton


class Button:
    def __init__(self, text: str, callback: str = None, url: str = None):
        self.text = text
        self.callback = callback
        self.url = url

    def render(self):
        if self.callback and len(self.callback.encode()) > 64:
            raise ValueError("callback_data exceeds 64 bytes")
        if self.url:
            return InlineKeyboardButton(text=self.text, url=self.url)
        return InlineKeyboardButton(text=self.text, callback_data=self.callback)
