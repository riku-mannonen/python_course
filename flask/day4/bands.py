from flask import Flask, render_template, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms.ext.sqlalchemy.orm import model_form

app = Flask(__name__)
app.secret_key = "shoo4Zie9Waingee5Nuughoh3thaej"
db = SQLAlchemy(app)

class Band(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, nullable=False)
	best_song = db.Column(db.String, nullable=False)

BandForm = model_form(Band, base_class=FlaskForm, db_session=db.session)

@app.before_first_request
def initDb():
	db.create_all()

@app.route("/add", methods=["GET", "POST"])
def addBand():
	form = BandForm()

	if form.validate_on_submit():
		band = Band()
		form.populate_obj(band)
		db.session.add(band)
		db.session.commit()
		flash("Band added")
		return redirect("/")
	return render_template("add.html",form=form)

@app.route("/")
def index():
	bands = Band.query.all()
	return render_template("index.html", bands=bands)

if __name__ == "__main__":
	app.run()
