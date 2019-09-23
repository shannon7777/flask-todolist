from models.base_model import BaseModel
from werkzeug.security import generate_password_hash
from flask_login import UserMixin, current_user
from app import app
import peewee as pw
import re 

class User(UserMixin, BaseModel):
    first_name = pw.CharField(unique=False, null=False)
    last_name = pw.CharField(unique=False, null=False)
    email = pw.CharField(unique=True, null=False)
    password = pw.CharField(unique=False, null=False)

    def validate(self):
        if len(self.email) < 10:
            self.errors.append('Email must be longer than 10 characters!')
        if len(self.password) < 6:
            self.errors.append('Password must be longer than 6 characters!')
        if not self.password:
            self.errors.append('You must enter a password!')
        if not re.match(r"^[p][b][k][d][f][2][:][s][h][a][2][5][6][:].{80}\b", self.password):
            # nest password validation here
            hashed_password = generate_password_hash(self.password)
            self.password = hashed_password
    