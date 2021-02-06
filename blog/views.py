from flask_blog import app, db
from flask import render_template, redirect, flash, url_for
from flask_blog.blog.form import SetupForm
from flask_blog.author.models import Author
from flask_blog.blog.models import Blog
from flask_blog.author.decorators import login_required
import bcrypt

@app.route('/')
@app.route('/index')
def index():
    blogs = Blog.query.count()
    if blogs == 0:
        return redirect(url_for('setup'))
    return "Hello World"


@app.route('/admin')
@login_required
def admin():
    return render_template('blog/admin.html')


@app.route('/setup', methods=('GET', 'POST'))
def setup():
    form = SetupForm()
    error = ''

    if form.validate_on_submit():
        salt = bcrypt.gensalt()
        h_pass = bcrypt.hashpw(form.password.data, salt)
        author = Author(
            form.fullname.data,
            form.email.data,
            form.username.data,
            h_pass,
            True
        )
        db.session.add(author)
        db.session.flush()
        if author.id:
            blog = Blog(
                form.name.data,
                author.id
            )
            db.session.add(blog)
            db.session.flush()
        else:
            db.session.rollback()
            error = 'Error creating user'
        if author.id and blog.id:
            db.session.flush()
            flash("Blog created")
            db.session.commit()
            return redirect(url_for('admin'))
        else:
            db.session.rollback()
            error = 'Error creating blog'
    db.session.commit()
    return render_template('blog/setup.html', form=form, error=error)

