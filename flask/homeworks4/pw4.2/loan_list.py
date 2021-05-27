from flask import Flask, render_template, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms.ext.sqlalchemy.orm import model_form
from datetime import datetime

app = Flask(__name__)
app.secret_key = "7jdjds+03lg__sadhhgsg12k9a7d79fkakf&&oa5Koh7t0a"
db = SQLAlchemy(app)

class Item(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	item = db.Column(db.String, nullable=False)
	borrower = db.Column(db.String, nullable=False)

ItemForm = model_form(Item, base_class=FlaskForm, db_session=db.session)

@app.before_first_request
def initDb():
	db.create_all()

@app.route("/edit/<int:id>", methods=["GET","POST"])
@app.route("/add", methods=["GET", "POST"])
def addItem(id=None):
	item = Item()
	if id:
		item = Item.query.get_or_404(id)

	form = ItemForm(obj=item)

	if form.validate_on_submit():
		form.populate_obj(item)
		db.session.add(item)
		db.session.commit()
		flash("Item added.")
		return redirect("/")
	return render_template("add.html", form=form)

@app.route("/delete/<int:id>")
def deleteItem(id):
	item = Item.query.get_or_404(id)
	db.session.delete(item)
	db.session.commit()

	flash("Deleted.")
	return redirect("/")

@app.route("/")
def index():
	items = Item.query.all()
	return render_template("index.html", items=items)

if __name__ == "__main__":
	app.run()
