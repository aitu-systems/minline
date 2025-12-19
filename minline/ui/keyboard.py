from aiogram.types import InlineKeyboardMarkup
from minline.ui.button import Button


def build_keyboard(layout: list) -> InlineKeyboardMarkup:
    keyboard = []
    for row in layout:
        keyboard.append([btn.render() for btn in row if isinstance(btn, Button)])
    return InlineKeyboardMarkup(inline_keyboard=keyboard)
