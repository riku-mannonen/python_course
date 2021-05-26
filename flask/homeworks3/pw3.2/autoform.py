from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

from flask_wtf import FlaskForm
from wtforms.ext.sqlalchemy.orm import model_form

app = Flask(__name__)
app.secret_key = "aiX3Zi£umosRi4a?be1aSSer3aet9eng"
db = SQLAlchemy(app)

class Band(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, nullable=False)
	genre = db.Column(db.String)

BandForm = model_form(Band, base_class=FlaskForm, db_session=db.session)

@app.before_first_request
def initMe():
	db.create_all()
	band = Band(name="Bolt Thrower", genre="death metal")
	db.session.add(band)

	band = Band(name="Paradise Lost", genre="doom metal")
	db.session.add(band)

	db.session.commit()

@app.route("/")
def index():
    bands = Band.query.all()
    return render_template("index.html", bands=bands)

@app.route("/add", methods=["GET", "POST"])
def addForm():
    form = BandForm()
    return render_template("add.html", form=form)

if __name__ == "__main__":
	app.run()
