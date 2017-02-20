from flask_blog.author.form import RegisterForm, LoginForm
from flask import render_template, redirect, url_for, session

from flask_blog import app


@app.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    error = None

    if form.validate_on_submit():
        pass

    return render_template('author/login.html', form=form, error=error)


@app.route('/register', methods=('GET', 'POST'))
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        form.p('hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello ')
        return redirect(url_for('success'))
    return render_template('author/register.html', form=form)


@app.route('/success')
def success():
    return "Author registered"
