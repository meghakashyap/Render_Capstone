from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from dotenv import dotenv_values
import os
from sqlalchemy.orm import declarative_base
from api import app


config = dotenv_values()
# Database URL (replace with your actual credentials)
database_path = database_path = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Initialize SQLAlchemy
db = SQLAlchemy()

# Define the  Movie model
class Movie(db.Model):
    __tablename__ = "movie"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    release_date = db.Column(db.DateTime)
    

# Define the Actor model
class Actor(db.Model):
    __tablename__ = "actor"
    id = db.Column(db.Integer, primary_key =True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    gender = db.Column(db.String)
    
    

# Create all tables
def create_tables():
    db.create_all()
    print("Tables created")

# Insert sample data
def insert_data():
    
    # Create Movie
    m1 = Movie(title="Red Notice", release_date="2021-02-02T14:30:00")
    m2 = Movie(title="Harry Potter", release_date="2001-02-02T14:30:00")
    
    # Add Moie to the session
    db.session.add_all([m1, m2])
    db.session.commit()

    # Create  Actors
    a1 = Actor(name="Sonam Kapoor", age=40, gender="female")
    a2 = Actor(name="Ranveer Kapoor", age=42, gender="male")
    a3 = Actor(name="Tom Cruise", age=40, gender="male")
    
    # Add menus to the session
    db.session.add_all([a1, a2, a3])
    db.session.commit()

    print("Data inserted")

if __name__ == '__main__':
    with app.app_context():
        create_tables()
        insert_data()
