
import os
from flask import app
from sqlalchemy import Column, String, Integer, create_engine, DateTime
from flask_sqlalchemy import SQLAlchemy
import json
from dotenv import dotenv_values
from config import Config


config = dotenv_values()
database_path = Config.database_url


db = SQLAlchemy()



"""
setup_db(app)
    binds a flask application and a SQLAlchemy service
"""


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    with app.app_context():
        db.create_all()
    # db.create_all()
    
    
# Movie
class Movie(db.Model):
    __tablename__ = "movie"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    release_date = db.Column(db.DateTime)
    
    def __init__(self,title,release_date):
        self.title = title
        self.release_date = release_date
        
    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def format(self):
        return {
            "id": self.id,
            "title":self.title,
            "release_date":self.release_date
            }

# Actor

class Actor(db.Model):
    __tablename__ = "actor"
    id = db.Column(db.Integer, primary_key =True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    gender = db.Column(db.String)
    
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
    def format(self):
        return {
            "id":self.id, 
            "name":self.name,
            "age":self.age, 
            "gender":self.gender
            }
    
