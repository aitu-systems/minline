from abc import ABC, abstractmethod
from typing import Any

class SessionManager(ABC):

    @abstractmethod
    def get(self, chat_id: int, key: str) -> Any | None:
        pass

    @abstractmethod
    def set(self, chat_id: int, key: str, value: Any) -> None:
        pass

    @abstractmethod
    def delete(self, chat_id: int, key: str) -> None:
        pass

    @abstractmethod
    def clear(self, chat_id: int) -> None:
        pass
