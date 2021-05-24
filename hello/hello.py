from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	return "Hei Riku!"

@app.route("/toinenreitti")
def toinen_sivu():
        return "Hei toisesta reitistä!"

app.run()
