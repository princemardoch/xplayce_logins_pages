from flask import(
    Blueprint, render_template, redirect, url_for
)

auth = Blueprint('auth', __name__)

@auth.route('/')
def main():
    return redirect(url_for('auth.login'))

@auth.route('/login')
def login():
    return 'TEST login route'

@auth.route('/signup')
def signup():
    return 'TEST signup route'

@auth.route('/logout')
def logout():
    return 'TEST logout route'