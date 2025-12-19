from minline import MinlineApp, Menu, Button

app = MinlineApp("BOT_TOKEN")

@app.route("/settings")
def settings():
    return Menu(
        menu_id="settings",
        controls=[
            [Button("Books", "#route:books")]
        ]
    )

@app.route("/settings/books")
def books():
    return Menu(
        menu_id="books",
        controls=[]
    )

app.run()