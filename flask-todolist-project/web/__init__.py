import random 
from app import app
from flask import render_template, abort, request, flash, redirect, url_for
from flask_assets import Environment, Bundle
from flask_login import LoginManager, current_user, login_required
from flask_wtf.csrf import CSRFProtect
from flask_cors import CORS
from .util.assets import bundles
from web.blueprints.users.views import users_blueprint
from web.blueprints.todos.views import todos_blueprint
from models.user import User
from models.todo import Todo

# CORS(app)
cors = CORS(app, resources={r"/todos/*": {"origins": "*"}})
# Assets
assets = Environment(app)
assets.register(bundles)

# CSRF Protect
# csrf = CSRFProtect(app)


# Login Manager & User Loader settings
login_manager = LoginManager(app)
@login_manager.user_loader
def load_user(id):
    return User.get_or_none(id=id)

login_manager.login_view = "sessions.login"
login_manager.login_message = u"You must be logged in to view this content."
login_manager.login_message_category = "danger"

# Registering Blueprints
app.register_blueprint(users_blueprint, url_prefix="/users")
app.register_blueprint(todos_blueprint, url_prefix="/todos")
# app.register_blueprint(sessions_blueprint, url_prefix="/sessions")

# Error Routes
# @app.errorhandler(404)
# def internal_server_error(e):
#     return render_template('404.html'), 404

# @app.errorhandler(500)
# def internal_server_error(e):
#     return render_template('500.html'), 500

# Routes
@app.route("/")
def home():
    return render_template('home.html')