from app import app
from flask import Blueprint, render_template, request, flash, redirect, url_for, session, jsonify
from models.todo import Todo
from models.list import List
from flask_cors import CORS, cross_origin
import json

todos_blueprint = Blueprint('todos', __name__, template_folder='templates')
# CORS(todos_blueprint)

@todos_blueprint.route('/', methods=['GET'])
def homepage():
    # lists = List.select().order_by(List.id.asc())
    # todos = Todo.select().order_by(Todo.id.asc())
    # make into array then can loop through it and will be JSON serializeable
    all_lists = [l.list_name for l in List.select().order_by(List.id.asc())]
    all_todos = [t.content for t in Todo.select().order_by(Todo.id.asc())]
    
    result = jsonify({'all_lists': all_lists, 'all_todos': all_todos})

    return result

@todos_blueprint.route('/create_list', methods=['POST'])
def create_list():
    data = request.get_json()
    list_name = data['list_name']
    new_list = List(list_name=list_name)

    if new_list.save():
        flash(f'Successfully created a new list,{ list_name }!', 'success')
    else:
        flash('Did not create a new list', 'danger')
    
    result = jsonify({'list_name': list_name})

    return result

@todos_blueprint.route('/create_todo', methods=['POST'])
def create_todo():
    data = request.get_json()
    content = data['content']
    new_todo = Todo(content=content, is_completed=False, list_id=6)
    
    if new_todo.save():
        flash('New to-do created!', 'success')
    else:
        flash('Unsuccessful', 'danger')
    
    result = jsonify({
        'message':'Todo created',
        'content': content
        })
    
    return result




