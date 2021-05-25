from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
	bands = ["Darkthrone", "Bolt Thrower", "Type O Negative", "Death", "Iron Maiden"]
	return render_template("list.html", bands=bands)

app.run()
