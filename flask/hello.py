from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("base.html")

@app.route("/toinenreitti")
def toinen_sivu():
        return "Hei toisesta reitistä!"

if __name__ == "__main__":
	app.run(debug=True)
