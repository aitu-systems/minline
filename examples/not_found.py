from minline import MinlineApp, Menu, Button

app = MinlineApp("BOT_TOKEN")

@app.route("/")
def main():
    return Menu(
        menu_id="main",
        controls=[
            [Button("Broken link", "#route:/does-not-exist")]
        ]
    )

app.run()