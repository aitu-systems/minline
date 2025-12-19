from aiogram.types import InlineKeyboardMarkup
from minline.ui.keyboard import build_keyboard
from minline.ui.button import Button


class Menu:
    def __init__(self, menu_id: str, controls: list, text: str | None = None, back: bool = True):
        self.menu_id = menu_id
        self.text = text or menu_id
        self.controls = controls
        self.back = back


    def render(self, show_back: bool) -> InlineKeyboardMarkup:
        layout = []

        if show_back and self.back:
            layout.append([Button("Back", "#route://")])

        layout.extend(self.controls)
        return build_keyboard(layout)

    @staticmethod
    def not_found(path: str):
        return Menu(
            menu_id=f'Page "{path}" does not exist',
            controls=[
                [Button("Docs", url="https://github.com/bakirullit/minline")]
            ],
            back=True
        )
