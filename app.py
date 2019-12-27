from flask import Flask, render_template,redirect, url_for, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from database import get_db, connect_db


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

@app.route('/', methods=['GET','POST'])
def index():
	if request.method == 'POST':
		db = get_db()
		db.execute('insert into project_enteries(name, email, message) values (?, ?, ?)',[request.form['name'],request.form['email'],request.form['message']])
		db.commit()
		flash("Thanks For Feeding the information We will reach to you soon", 'success')
		return redirect(url_for('index'))

	return render_template('index.html', title='Aman Malhotra')

if __name__ == '__main__':
	app.run(debug=True)