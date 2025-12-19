from minline import MinlineApp, Menu, Button

app = MinlineApp("BOT_TOKEN")

@app.route("/")
def main():
    return Menu(
        menu_id="main",
        controls=[
            [Button("Settings", "#route:/settings")]
        ]
    )

@app.route("/settings")
def settings():
    return Menu(
        menu_id="settings",
        controls=[]
    )

app.run()