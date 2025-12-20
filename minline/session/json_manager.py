import json
import threading
from pathlib import Path

from minline.session.base import SessionManager


class JsonSessionManager(SessionManager):
    def __init__(self, path: str = "sessions.json"):
        self.file = Path(path)
        self.lock = threading.Lock()

        if not self.file.exists():
            self.file.write_text("{}")

    def _load(self) -> dict:
        return json.loads(self.file.read_text())

    def _save(self, data: dict):
        self.file.write_text(json.dumps(data, indent=2))

    def get(self, chat_id: int, key: str):
        with self.lock:
            data = self._load()
            return data.get(str(chat_id), {}).get(key)

    def set(self, chat_id: int, key: str, value):
        with self.lock:
            data = self._load()
            user = data.setdefault(str(chat_id), {})
            user[key] = value
            self._save(data)

    def delete(self, chat_id: int, key: str):
        with self.lock:
            data = self._load()
            user = data.get(str(chat_id))
            if not user:
                return
            user.pop(key, None)
            self._save(data)

    def clear(self, chat_id: int):
        with self.lock:
            data = self._load()
            data.pop(str(chat_id), None)
            self._save(data)
