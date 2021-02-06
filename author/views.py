from flask_blog.author.form import RegisterForm, LoginForm
from flask import render_template, redirect, url_for, session, request
from flask_blog.author.models import Author
from flask_blog.author.decorators import login_required
import bcrypt
from flask_blog import app


@app.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    error = None

    req = request.args.get('next')
    if request.method == 'GET' and req:
        session['next'] = req

    if form.validate_on_submit():
        user = form.username.data
        authors = Author.query.filter_by(
            username=user
        ).limit(1)

        if authors.count:
            author = authors[0]
            print(form.password.data)
            print(bcrypt.hashpw(form.password.data. author.password))
            if bcrypt.hashpw(form.password.data. author.password) == author.password:
                session['username'] = user
                if 'next' in session:
                    _next = session['next']
                    session.pop('next')
                    return redirect(_next)
                else:
                    return redirect(url_for('success'))
            else:
                error = 'Incorrect username password'
        else:
            error = 'Incorrect username and/or password'
    return render_template('author/login.html', form=form, error=error)


@app.route('/register', methods=('GET', 'POST'))
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        form.p('hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello ')
        return redirect(url_for('success'))
    return render_template('author/register.html', form=form)


@app.route('/success')
@login_required
def success():
    return "Author registered"
