from app import app

from flask import render_template


@app.route("/")
def index():
    return render_template("public/index.html")

@app.route("/jinja")
def jinja():
    name = "Anandhu Remanan"

    subjects = ["Computer Science", "Math", "English", "Malayalam"]

    return render_template("public/jinja.html", name=name, subjects=subjects)