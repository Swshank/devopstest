from flask import Flask

app = Flask(__name__)

def add(a, b):
    return a + b

@app.route("/")
def home():
    return "Hello from Azure App Service! 🚀"

@app.route("/add/<int:a>/<int:b>")
def add_route(a, b):
    return str(add(a, b))

if __name__ == "__main__":
    app.run()
