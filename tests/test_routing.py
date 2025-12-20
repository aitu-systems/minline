from minline.routing.stack import NavigationStack
from minline.routing.utils import parent_path

# Mock of your MinlineApp nav methods
class TestApp:
    def __init__(self):
        self.nav = NavigationStack()

    def current_path(self, user_id) -> str:
        return self.nav.current(user_id)

    def can_go_back(self, user_id) -> bool:
        return self.current_path(user_id) != "/"

    def parent_path(self, path: str) -> str:
        return parent_path(path)


# Test
app = TestApp()
user_id = 1

# Push some paths
app.nav.push(user_id, "/")
app.nav.push(user_id, "/settings")
app.nav.push(user_id, "/settings/notifications")

print("Current Path:", app.current_path(user_id))  # /settings/notifications
print("Can Go Back:", app.can_go_back(user_id))    # True
print("Parent Path:", app.parent_path("/settings/notifications"))  # /settings

# Pop back
app.nav.back(user_id)
print("After back, Current Path:", app.current_path(user_id))  # /settings
print("Can Go Back:", app.can_go_back(user_id))               # True
