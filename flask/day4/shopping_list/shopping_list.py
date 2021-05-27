from flask import Flask, render_template, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms.ext.sqlalchemy.orm import model_form

app = Flask(__name__)
app.secret_key = "AethocoKahcaex8aehooLahvahHebaNieho"
db = SQLAlchemy(app)

class Item(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, nullable=False)
	quantity = db.Column(db.Integer)

ItemForm = model_form(Item, base_class=FlaskForm, db_session=db.session)

@app.before_first_request
def initDb():
	db.create_all()

@app.route("/add", methods=["GET","POST"])
def addItem():
	form = ItemForm()

	if form.validate_on_submit():
		item = Item()
		form.populate_obj(item)
		db.session.add(item)
		db.session.commit()
		flash("Item added to shopping list.")
		return redirect("/")
	return render_template("add.html", form=form)

@app.route("/")
def index():
	items = Item.query.all()
	return render_template("index.html", items=items)

if __name__ == "__main__":
	app.run()
