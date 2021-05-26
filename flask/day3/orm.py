from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy

from flask_wtf import FlaskForm
from wtforms.ext.sqlalchemy.orm import model_form

app = Flask(__name__)
app.secret_key = "aiX3Zi0umohRiXaebegaer3aet9eng"
db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    genre = db.Column(db.String)

MovieForm = model_form(Movie, base_class=FlaskForm, db_session=db.session)

@app.before_first_request
def initMe():
	db.create_all()
	movie = Movie(name="Demons", genre="horror")
	db.session.add(movie)

	movie = Movie(name="Great Silence", genre="western")
	db.session.add(movie)

	db.session.commit()

@app.route("/msg")
def msgPage():
    flash("Here is a message for you!")
    return redirect("/")

@app.route("/new", methods=["GET", "POST"])
def addForm():
    form = MovieForm()
    print(request.form) # test only
    return render_template("new.html", form=form)

@app.route("/")
def index():
    movies = Movie.query.all()
    return render_template("index.html", movies=movies)

if __name__ == "__main__":
	app.run()
