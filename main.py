from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/offices.html")
def offices():
    return render_template("offices.html")


@app.route("/services")
def services():
    return render_template("services.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(host='127.0.0.0', port=5000)
