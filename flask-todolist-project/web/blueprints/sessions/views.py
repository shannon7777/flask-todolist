from app import app
from flask import Blueprint, render_template, redirect, url_for, request, flash

sessions_blueprint = Blueprint('sessions', __name__, template_folder='templates')


@sessions_blueprint.route('/new', methods=['GET'])
def new():
    return render_template('/sessions/new.html')