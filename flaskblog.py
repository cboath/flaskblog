from flask import Flask, render_template, url_for, flash
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '9dj2576340d1a8fg03jg93k302385023'

posts = [
    {
        'author': 'Teater',
        'title': 'B P 1',
        'content': 'All the words!',
        'date_posted': 'October 8, 2018'
    },
    {
        'author': 'Schrum',
        'title': 'B P 2',
        'content': 'Some of the words!',
        'date_posted': 'October 6, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html', posts=posts)
	
@app.route("/about")
def about():
	return render_template('about.html', title='About')
    
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Account created for {form.username.data}!', 'success')
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)
	
	
if __name__ == '__main__':
	app.run(debug=True)
