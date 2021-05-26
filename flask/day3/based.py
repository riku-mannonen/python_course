from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

class Comment(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	text = db.Column(db.String, nullable=False)
	name = db.Column(db.String, nullable=False)

class Task(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	text = db.Column(db.String, nullable=False)
	name = db.Column(db.String, nullable=False)

@app.before_first_request
def initMe():
	db.create_all()

	comment = Comment(text="Have a nice day!", name= "Riku")
	db.session.add(comment)

	comment = Comment(text="Cold winds are rising", name= "Nuutti")
	db.session.add(comment)

	task = Task(text="Go to gym", name= "Riku")
	db.session.add(task)

	task = Task(text="Cook some food", name="Riku")
	db.session.add(task)

	db.session.commit()

@app.route("/")
def index():
	comments = Comment.query.all()
	tasks = Task.query.all()
	return render_template("index.html", comments=comments, tasks=tasks)

if __name__ == "__main__":
	app.run()

