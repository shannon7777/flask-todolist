from app import app
from models.base_model import BaseModel
from models.list import List
import peewee as pw

class Todo(BaseModel):
    content = pw.TextField(null=True, unique=False)
    is_completed = pw.BooleanField(default=False)
    list_id = pw.ForeignKeyField(List, backref='todos', null=True, on_delete='CASCADE')

    # def as_dict(self):
    #     json_dict = {
    #         'content': self.content,
    #         'is_completed': self.is_completed,
    #         'list_id': self.list_id
    #     }
    #     return json_dict