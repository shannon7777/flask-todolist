from app import app
from models.base_model import BaseModel
import peewee as pw

class List(BaseModel):
    list_name = pw.CharField(null=True, unique=True)
