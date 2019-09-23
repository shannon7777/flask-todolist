import datetime
from app import app
from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.utils import secure_filename
from models.user import User


users_blueprint = Blueprint('users', __name__, template_folder='templates')


@users_blueprint.route('/new', methods=['GET'])
def new():
    return render_template('/users/new.html')

@users_blueprint.route('/<username>', methods=['GET'])
@login_required
def show(username):
    user = User.get(User.username == current_user.username)
    return render_template('/users/show.html', username=user.username)

@users_blueprint.route('/', methods=['POST'])
def create():
    email = request.form.get('email')
    password = request.form.get('password')
    user = User(email=email, password=password)

    if user.save():
        login_user(user)
        flash("Your account was successfully created.", "success")
        return redirect(url_for('home'))
    else:
        flash("Your account could not be created. Please fix the errors and try again.", "danger")
        return redirect(url_for('sessions.login', errors=user.errors))

@users_blueprint.route('/update/<id>', methods=['POST'])
@login_required
def update(id):
    user = User.get_by_id(id)
    if current_user == user:
        if request.form.get('username'):
            user.username = request.form.get('username')
        if request.form.get('email'):
            user.email = request.form.get('email')
        if request.form.get('first_name'):
            user.first_name = request.form.get('first_name')
        if request.form.get('last_name'):
            user.last_name = request.form.get('last_name')

        if user.save():
            flash("Your profile information has been updated", "success")
            return redirect(url_for('users.show', username=user.username))
        else:
            flash("Your information was not updated. Please try again.", "danger")
            return redirect(url_for('users.show', username=user.username))
