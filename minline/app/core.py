import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup

from minline.session import SessionManager, JsonSessionManager, MessageManager, SessionKeys

from minline.app.commands.context import CommandContext
from minline.app.commands.registry import CommandRegistry

from aiogram.filters import CommandStart
from aiogram.types import Message

from minline.routing import (
    RouteResolver,
    NavigationStack,
    NavigationProtocol,
)

class MinlineApp:
    def __init__(self, token: str, session_manager: SessionManager = None):
        self.bot = Bot(token)
        self.dp = Dispatcher()
        self.routes = RouteResolver()
        self.nav = NavigationStack()
        self.nav_protocol = NavigationProtocol()
        self.commands = CommandRegistry()
        self.session: SessionManager = session_manager or JsonSessionManager("sessions.json")
        self.messages = MessageManager(self.session)
        self.is_404 = {}

        @self.dp.message(CommandStart())
        async def _start(msg: Message):
            await self._render(msg, "/", source="start")

        @self.dp.message()
        async def my_custom_handler(msg: Message):
            path = "/custom"
            await self._render(msg, path)

        @self.dp.callback_query()
        async def callback(cb: types.CallbackQuery):
            data = cb.data

            if data.startswith(self.nav_protocol.BACK):
                path = self.nav.current(cb.message.chat.id) if self.is_404.get(cb.message.chat.id) else self.nav.back(cb.message.chat.id)
                await self._render(cb, path, push=False)
                return

            if data.startswith(self.nav_protocol.ROUTE):
                raw = data.replace(self.nav_protocol.ROUTE, "")
                base = self.nav.current(cb.message.chat.id).rstrip("/")
                path = raw if raw.startswith("/") else f"{base}/{raw}"
                await self._render(cb, path, push=True)
                return

            await cb.answer("Action executed")




    def route(self, path: str):
        def decorator(func):
            self.routes.register(path, func)
            return func
        return decorator

    def command(self, name: str):
        def decorator(func):
            self.commands.register(name, func)
            return func
        return decorator

    async def _render(self, msg_obj: types.Message | types.CallbackQuery, path: str, push=True, source=None):
        if isinstance(msg_obj, types.Message):
            chat_id = msg_obj.chat.id
        elif isinstance(msg_obj, types.CallbackQuery):
            chat_id = msg_obj.message.chat.id
        else:
            raise TypeError("msg_obj must be Message or CallbackQuery")

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

        last_id = self.messages.get(chat_id)

        if isinstance(msg_obj, types.Message):
            try:
                await msg_obj.delete()
            except Exception:
                pass
        elif isinstance(msg_obj, types.CallbackQuery):
            try:
                await msg_obj.message.delete()
            except Exception:
                pass

        if last_id:
            try:
                await self.bot.edit_message_text(chat_id=chat_id, message_id=last_id,
                                                text=menu.menu_id, reply_markup=markup)
                self.messages.set(chat_id, last_id)
                return
            except Exception:
                try:
                    await self.bot.delete_message(chat_id, last_id)
                except Exception:
                    pass

        msg = await self.bot.send_message(chat_id, menu.menu_id, reply_markup=markup)
        self.messages.set(chat_id, msg.message_id)



    def current_path(self, user_id) -> str:
        return self.nav.get(user_id)

    def can_go_back(self, user_id) -> bool:
        return self.current_path(user_id) != "/"

    def parent_path(self, path: str) -> str:
        return parent_path(path)
        
    def run(self):
        asyncio.run(self.dp.start_polling(self.bot))
