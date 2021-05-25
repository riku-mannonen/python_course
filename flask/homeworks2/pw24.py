from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def forms():
        return render_template("forms.html")

app.run()
