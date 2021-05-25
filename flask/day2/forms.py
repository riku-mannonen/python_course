from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def forms():
        return render_template("forms3.html")

@app.route("/post")
def post():
	return render_template("forms.html")

@app.route("/get")
def get():
        return render_template("forms2.html")

app.run()
