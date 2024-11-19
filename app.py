from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def index():
    fruits = [
        {"name": "apples", "quantity": 3},
            {"name": "oranges", "quantity": 2},
            {"name": "strawberries", "quantity": 6}
    ]
    for fruit in fruits:
        if not fruit["name"].startswith("o"):
            fruits.remove(fruit)
        if fruit["quantity"] < 1:
            fruits.remove(fruit)

    return render_template("index.html", fruits=fruits)
