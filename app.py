from flask import Flask, render_template, url_for, redirect, request, session
from user.models import User, Term
from functools import wraps
from flask_paginate import Pagination, get_page_args

import db

app = Flask(__name__)
app.secret_key = '1a2b3c4d5e6f7g'

PER_PAGE = 5


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/')

    return wrap


def paginate(terms):
    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page')
    offset = page * PER_PAGE - PER_PAGE
    return terms[offset: offset + PER_PAGE]


def pagination_args(terms):
    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page')
    total = len(terms)
    return Pagination(page=page, per_page=PER_PAGE, total=total, css_framework='bulma')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register')
def register_page():
    return render_template('register.html')


@app.route('/user/register', methods=['POST'])
def register():
    return User().register()


@app.route('/user/login', methods=['POST'])
def login():
    return User().login()


@app.route('/user/logout')
def logout():
    return User().logout()


@app.route('/dashboard/')
@login_required
def dashboard():
    terms = Term().get_all()

    terms_paginate = paginate(terms)
    pagination = pagination_args(terms)

    return render_template('dashboard.html', terms=terms_paginate, pagination=pagination)


@app.route('/search/<term>')
@login_required
def search(term):
    return Term().get(term)


@app.route('/create', methods=['POST'])
@login_required
def create():
    return Term().create()


@app.route('/my-terms')
@login_required
def my_terms():
    data = User().get_my_terms()
    print(data)
    return render_template('user_terms.html', data=data)


@app.route('/edit/<term>', methods=['POST'])
@login_required
def edit(term):
    return Term().edit(term)


@app.route('/delete/<term>', methods=["POST"])
@login_required
def delete(term):
    return Term().delete(term)
