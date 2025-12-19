---

## `README.md`

```md
# Minline

Minline is a lightweight navigation-first framework built on top of **aiogram 3.x** for creating Telegram bots with **structured menus**, **relative routing**, and **stateful navigation**.

It is designed for developers who want:
- deterministic menu routing
- zero magic strings scattered across handlers
- scalable menu hierarchies
- predictable back navigation

Minline treats bot UI as a **routing problem**, not a callback mess.

---

## Core Concepts

### 1. Routes

Routes are hierarchical paths, similar to URLs:

```

/
└── settings
└── books

````

Each route maps to a function returning a `Menu`.

```python
@app.route("/settings/books")
def books():
    ...
````

---

### 2. Navigation Protocol

Minline defines a strict navigation protocol:

| Action         | Syntax             | Meaning                |
| -------------- | ------------------ | ---------------------- |
| Absolute route | `#route:/settings` | Jump to exact path     |
| Relative route | `#route:books`     | Append to current path |
| Back           | `#route://`        | Go to previous path    |

These constants are centralized in `NavigationProtocol`.

---

### 3. Relative Routing

If current route is:

```
/settings
```

Then:

```python
Button("Books", "#route:books")
```

Resolves to:

```
/settings/books
```

No manual string concatenation. No guessing.

---

### 4. Automatic Back Button

Menus automatically receive a **Back** button when:

* route is not `/`
* `auto_back=True` (default)

You can disable it per menu.

---

### 5. 404 Handling

Unknown routes do not crash the bot.

Instead:

* previous route is preserved
* user sees a Not Found menu
* Back always returns safely

---

## Minimal Example

```python
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
```

---

## Design Philosophy

* Navigation is **data**, not callbacks
* Routing is **explicit**
* Back behavior is **deterministic**
* Menus are **pure objects**
* aiogram is infrastructure, not architecture

Minline does not fight Telegram.
It just refuses to pretend callbacks are a routing system.

---

## Status

This project is under active refactoring.
APIs are stabilizing.
Expect clarity, not backward compatibility.

```

---

## `examples/` directory

Create this structure:

```

examples/
├── basic.py
├── relative_routing.py
├── auto_back.py
├── hide_back.py
├── not_found.py

````

---

### `examples/basic.py`

```python
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
````

---

### `examples/relative_routing.py`

```python
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
```

---

### `examples/auto_back.py`

```python
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
```

Back buttons appear automatically on level1 and level2.

---

### `examples/hide_back.py`

```python
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
```

---

### `examples/not_found.py`

```python
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
```

---
