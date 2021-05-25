from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
	hats = ["ninja hood", "cap", "helmet"]
	return render_template("hello.html", hats=hats)

app.run()
