from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
	animals = ["cat", "dog"]
	return render_template("condition.html", animals=animals)

app.run()
