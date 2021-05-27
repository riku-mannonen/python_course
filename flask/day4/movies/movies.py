from flask import Flask, render_template, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms.ext.sqlalchemy.orm import model_form
from datetime import datetime

app = Flask(__name__)
app.secret_key = "shoighaish2teoYoa5Koh7eo4iex9aemee1eet0a"
db = SQLAlchemy(app)

class Movie(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, nullable=False)

MovieForm = model_form(Movie, base_class=FlaskForm, db_session=db.session)

@app.before_first_request
def initDb():
	db.create_all()

@app.route("/<int:id>/edit", methods=["GET","POST"])
@app.route("/add", methods=["GET", "POST"])
def addMovie(id=None):
	movie = Movie()
	if id:
		movie = Movie.query.get_or_404(id)

	form = MovieForm(obj=movie)

	if form.validate_on_submit():
		form.populate_obj(movie)
		db.session.add(movie)
		db.session.commit()
		flash("Movie added.")
		return redirect("/")
	return render_template("add.html", form=form)

@app.route("/<int:id>/delete")
def deleteMovie(id):
	movie = Movie.query.get_or_404(id)
	db.session.delete(movie)
	db.session.commit()

	flash("Deleted.")
	return redirect("/")

@app.route("/")
def index():
	movies = Movie.query.all()
	return render_template("index.html", movies=movies)

if __name__ == "__main__":
	app.run()
