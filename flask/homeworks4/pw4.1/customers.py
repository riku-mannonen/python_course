from flask import Flask, render_template, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms.ext.sqlalchemy.orm import model_form
from datetime import datetime

app = Flask(__name__)
app.secret_key = "shoighaish2teoYoa5Koh7eo4iex9aemee1eet0a"
db = SQLAlchemy(app)

class Customer(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String, nullable=False)
	last_name = db.Column(db.String, nullable=False)
	email = db.Column(db.String, nullable=False)
	address = db.Column(db.String, nullable=False)
	phone_number = db.Column(db.String, nullable=False)

CustomerForm = model_form(Customer, base_class=FlaskForm, db_session=db.session)

@app.before_first_request
def initDb():
	db.create_all()

@app.route("/edit/<int:id>", methods=["GET","POST"])
@app.route("/add", methods=["GET", "POST"])
def addCustomer(id=None):
	customer = Customer()
	if id:
		customer = Customer.query.get_or_404(id)

	form = CustomerForm(obj=customer)

	if form.validate_on_submit():
		form.populate_obj(customer)
		db.session.add(customer)
		db.session.commit()
		flash("Customer added.")
		return redirect("/")
	return render_template("add.html", form=form)

@app.route("/delete/<int:id>")
def deleteCustomer(id):
	customer = Customer.query.get_or_404(id)
	db.session.delete(customer)
	db.session.commit()

	flash("Deleted.")
	return redirect("/")

@app.route("/")
def index():
	customers = Customer.query.all()
	return render_template("index.html", customers=customers)

if __name__ == "__main__":
	app.run()
