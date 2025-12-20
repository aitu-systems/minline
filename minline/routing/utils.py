def parent_path(path: str) -> str:
    if path == "/":
        return "/"
    return "/" + "/".join(path.strip("/").split("/")[:-1])

def normalize_path(path: str) -> str:
    if not path.startswith("/"):
        path = "/" + path
    return path.rstrip("/") or "/"

def resolve_relative(base: str, relative: str) -> str:
    return normalize_path(f"{base}/{relative}")
