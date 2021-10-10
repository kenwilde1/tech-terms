from flask import Flask, render_template, url_for, redirect, request, session
from user.models import User, Term
from functools import wraps
import pymongo

import db

app = Flask(__name__)
app.secret_key = '1a2b3c4d5e6f7g'

# Decorators


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/')

    return wrap


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
    return render_template('dashboard.html')


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
