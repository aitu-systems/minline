from minline import MinlineApp, Menu, Button

app = MinlineApp("BOT_TOKEN")

@app.route("/")
def root():
    return Menu(
        menu_id="root",
        controls=[
            [Button("Go deeper", "#route:/level1")]
        ]
    )

@app.route("/level1")
def level1():
    return Menu(
        menu_id="level1",
        controls=[
            [Button("Next", "#route:level2")]
        ]
    )

@app.route("/level1/level2")
def level2():
    return Menu(
        menu_id="level2",
        controls=[]
    )

app.run()