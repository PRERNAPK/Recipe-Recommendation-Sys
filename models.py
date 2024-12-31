from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import UserMixin


db = SQLAlchemy()
bcrypt = Bcrypt()

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    cuisine = db.Column(db.String(50))
    ingredients = db.Column(db.String(500))  # Comma-separated ingredients
    instructions = db.Column(db.Text)
    prep_time = db.Column(db.String(10))  # In minutes
    image_url = db.Column(db.String(120), nullable=True)
    def __repr__(self):
        return f"<Recipe {self.name}>"
    
class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

