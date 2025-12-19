class RouteResolver:
    def __init__(self):
        self.routes = {}

    def register(self, path: str, handler):
        self.routes[self._norm(path)] = handler

    def resolve(self, path: str):
        return self.routes.get(self._norm(path))


    def _norm(self, path: str):
        return "/" if path == "/" else path.rstrip("/")
