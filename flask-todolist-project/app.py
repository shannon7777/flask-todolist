import os
import config
from flask import Flask
from flask_cors import CORS
from models.base_model import db

# Change 'web' to project name.
web_dir = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'web')
# Change 'PROJECT' to project name.
app = Flask('flask-todolist-project', root_path=web_dir)

app.config['CORS_HEADERS'] = 'application/json'

if os.getenv('FLASK_ENV') == 'production':
    app.config.from_object("config.ProductionConfig")
else:
    app.config.from_object("config.DevelopmentConfig")

@app.before_request
def before_request():
    db.connect()

@app.after_request
def after_request(response):
    db.close()
    return response
