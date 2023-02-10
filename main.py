from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def greet() -> str:
    "Greet the user"
    return "Welcome to my flask project"


if __name__ == "__main__":
    app.run(debug=True)
