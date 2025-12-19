import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup

from minline.routing.resolver import RouteResolver
from minline.routing.stack import NavigationStack

from .protocol import NavigationProtocol

class MinlineApp:
    def __init__(self, token: str):
        self.bot = Bot(token)
        self.dp = Dispatcher()
        self.routes = RouteResolver()
        self.nav = NavigationStack()
        self.nav_protocol = NavigationProtocol()
        self.is_404 = {}

        @self.dp.message(CommandStart())
        async def start(msg: types.Message):
            await self._render(msg.chat.id, "/")

        @self.dp.callback_query()
        async def callback(cb: types.CallbackQuery):
            data = cb.data
            chat_id = cb.message.chat.id

            if data.startswith(self.nav_protocol.BACK):
                if self.is_404.get(chat_id):
                    path = self.nav.current(chat_id)
                    await self._render(chat_id, path, cb, push=False)
                else:
                    path = self.nav.back(chat_id)
                    await self._render(chat_id, path, cb, push=False)
                return


            if data.startswith(self.nav_protocol.ROUTE):
                raw = data.replace(self.nav_protocol.ROUTE, "")
                if raw.startswith("/"):
                    path = raw
                else:
                    base = self.nav.current(chat_id).rstrip("/")
                    path = f"{base}/{raw}"

                await self._render(chat_id, path, cb, push=True)
                return

            await cb.answer("Action executed")


    def route(self, path: str):
        def decorator(func):
            self.routes.register(path, func)
            return func
        return decorator

    async def _render(self, chat_id: int, path: str, cb=None, push=True):
        handler = self.routes.resolve(path)

        if handler is None:
            from minline.routing.menu import Menu
            menu = Menu.not_found(path)
            self.is_404[chat_id] = True
            push = False
            show_back = True
        else:
            menu = handler()
            self.is_404[chat_id] = False
            show_back = path != "/"

        if push:
            self.nav.push(chat_id, path)

        markup = menu.render(show_back=show_back)

        if cb:
            try:
                await cb.message.edit_text(menu.menu_id, reply_markup=markup)
            except Exception:
                pass
            await cb.answer()
        else:
            await self.bot.send_message(chat_id, menu.menu_id, reply_markup=markup)

    def run(self):
        asyncio.run(self.dp.start_polling(self.bot))
