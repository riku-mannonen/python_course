from flask import Flask, render_template, redirect, flash

app = Flask(__name__)
app.secret_key = "lLX3Zi01q5&UL0=)aaXaebegnw6%3aet9rus"

@app.route("/")
def index():
    return render_template("base.html")

@app.route("/one")
def one():
    flash("Valar morghulis")
    return redirect("/")

@app.route("/two")
def two():
    flash("Valar dohaeris")
    return redirect("/")

if __name__ == "__main__":
	app.run()
