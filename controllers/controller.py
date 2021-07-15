from app import app

@app.route('/')
def index():
    return "Hello from the otherside"

@app.route('/<name>')
def greet(name):
    return f"Hello {name}!"


@app.route("/greeting")
def greeting():
    return "Greetings, Everyone"


