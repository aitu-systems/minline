from minline import MinlineApp, Menu, Button

app = MinlineApp("BOT_TOKEN")

@app.route("/fullscreen")
def fullscreen():
    return Menu(
        menu_id="fullscreen",
        controls=[
            [Button("Exit", "#route:/")]
        ],
        auto_back=False
    )

app.run()