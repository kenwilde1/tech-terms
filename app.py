from flask import Flask, render_template, redirect, session, url_for
from user.models import User, Term
from functools import wraps
from flask_paginate import Pagination, get_page_args

import db

app = Flask(__name__)
app.secret_key = '1a2b3c4d5e6f7g'

PER_PAGE = 5


def login_required(f):
    """
    Ensures the User is logged in to access a route.
    """
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/')

    return wrap


@app.route('/')
def index():
    """
    Allow User to login.
    """
    return render_template('index.html')


@app.route('/register')
def register_page():
    """
    Allow User to register an account.
    """
    return render_template('register.html')


@app.route('/user/register', methods=['POST'])
def register():
    """
    Register a User with MongoDB.
    """
    return User().register()


@app.route('/user/login', methods=['POST'])
def login():
    """
    Check credentials with MongoDB and login User.
    """
    return User().login()


@app.route('/user/logout')
def logout():
    """
    Clears session and logs User out of system.
    """
    return User().logout()


@app.route('/dashboard/')
@login_required
def dashboard():
    """
    Returns a list of all created Terms and displays them in a table.
    """
    terms = Term().get_all()

    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page')
    offset = page * PER_PAGE - PER_PAGE
    terms_paginate = terms[offset: offset + PER_PAGE]

    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page')
    pagination = Pagination(page=page, per_page=PER_PAGE,
                            total=len(terms), css_framework='bulma')

    return render_template('dashboard.html', terms=terms_paginate, pagination=pagination)


@app.route('/search/<term>')
@login_required
def search(term):
    """
    Find a term definition.
    """
    return Term().get(term)


@app.route('/create', methods=['POST'])
@login_required
def create():
    """
    Create a term definition.
    """
    return Term().create()


@app.route('/my-terms')
@login_required
def my_terms():
    """
    Get User's term definitions.
    """
    data = User().get_my_terms()
    return render_template('user_terms.html', data=data)


@app.route('/edit/<term>', methods=['POST'])
@login_required
def edit(term):
    """
    Edit a term definition.
    """
    return Term().edit(term)


@app.route('/delete/<term>', methods=["POST"])
@login_required
def delete(term):
    """
    Delete a term definition.
    """
    return Term().delete(term)
