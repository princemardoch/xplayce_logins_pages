from flask import (
    Blueprint, Flask, render_template, redirect, url_for
)

user = Blueprint('user', __name__)

@user.route('/')
def index():
    return redirect(url_for('user.success_create'))

@user.route('/success')
def success_create():
    return 'Success create'