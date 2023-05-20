from random import randint

import eel

eel.init("web")


# Exposing the random_python function to javascript
@eel.expose
def random_python():
    print("Random function running")
    return randint(1, 100)


@eel.expose
def read_logs(path):
    try:
        with open(path, "r") as f:
            return {"status": "success", "logs": f.readlines()}
    except FileNotFoundError:
        return {"status": "error", "logs": []}


# Start the index.html file
eel.start("index.html", size=(800, 500))
