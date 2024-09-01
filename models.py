from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    actors = db.Column(db.String(200), nullable=False)
    director = db.Column(db.String(100), nullable=False)
    length = db.Column(db.Integer, nullable=False)  
    rating = db.Column(db.Float, nullable=False)
    feel = db.Column(db.String(100), nullable=False)  

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    preferences = db.Column(db.String(200), nullable=False)
