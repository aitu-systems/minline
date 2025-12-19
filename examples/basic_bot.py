from minline import MinlineApp, Menu, Button

app = MinlineApp("8124229474:AAG5tv1zBNvRlk5inmADom88SF72OE4Q-_c")


@app.route("/")
def main_menu():
    return Menu(
        menu_id="main",
        controls=[
            [Button("Settings", "#route:/settings")],
            [Button("Open Web", url="https://example.com")]
        ]
    )

@app.route("/settings")
def settings_menu():
    return Menu(
        menu_id="settings",
        controls=[
            [Button("Notifications", "toggle_notifications")],
            [Button("No File", "#route:book")],
            [Button("Books", "#route:books")]
        ]
    )

@app.route("/settings/books")
def books_menu():
    return Menu(
        menu_id="books",
        controls=[
            [Button("Open", "#route:open")],
            [Button("Back", "#route://")]
        ],
        back=False
    )

app.run()
