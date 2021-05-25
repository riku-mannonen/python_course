from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
	return render_template("variables.html", title="Hei maailma")

app.run()
