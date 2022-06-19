from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '41d40610130d3527998076436ce153f9'

posts = [
    {
        'author': 'Corey',
        'title': 'First post',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
     {
        'author': 'James',
        'title': 'Second post',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About Page')    

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if(form.email.data == 'zain@gmail.com' and form.password.data == '123456'):
            flash('You have been logged in', 'success')
            return redirect(url_for('home'))

        else:
            flash('Login Unsuccessful', 'danger')    
    return render_template('login.html', title='Login', form=form)        

if __name__ == '__main__':
    app.run(debug=True)