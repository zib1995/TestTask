

from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:password@localhost:5432/cats"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Cats(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	breed = db.Column(db.String(100))
	name = db.Column(db.String(100))
	age = db.Column(db.Integer())
	description = db.Column(db.String(500))
	picture = db.Column(db.String(100))
	
	def __repr__(self):
		return f"<users {self.id}>"
#


def get_catlist():
	cats = Cats.query.all()
	catlist = []
	num = 0
	for cat in cats:
		c = {
			'breed': cat.breed,
			'name': cat.name,
			'age': cat.age,
			'description': cat.description,
			'picture': cat.picture,
			'num': num
		}
		catlist.append(c)
		num += 1
	return catlist
#

catlist = []

@app.route('/')
@app.route('/index')
def hello():
	return render_template('index.html', items = catlist)
#

@app.route('/this_cat/<int:number>')
def cat_page(number):
	return render_template('about.html', item = catlist[number])
#

if __name__ == '__main__':
	global catlist
	catlist = get_catlist()
	app.run(host='0.0.0.0')
#
