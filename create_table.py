from sqlalchemy import create_engine, Column, Integer, String, Text, Numeric, Boolean, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from flask_sqlalchemy import SQLAlchemy
from dotenv import dotenv_values
import os
from sqlalchemy.orm import declarative_base


config = dotenv_values()
# Database URL (replace with your actual credentials)
database_path = config['DATABASE_URL']

# Create a new SQLAlchemy engine instance
engine = create_engine(database_path, echo=True)

# Base class for declarative models
Base = declarative_base()


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
    Base.metadata.create_all(engine)
    print("Tables created")

# Insert sample data
def insert_data():
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Create Movie
    m1 = Movie(title="Red Notice", release_date="2021-02-02T14:30:00")
    m2 = Movie(title="Harry Potter", release_date="2001-02-02T14:30:00")
    
    # Add Moie to the session
    session.add_all([m1, m2])
    session.commit()

    # Create  Actors
    a1 = Actor(name="Sonam Kapoor", age=40, gender="female")
    a2 = Actor(name="Ranveer Kapoor", age=42, gender="male")
    a3 = Actor(name="Tom Cruise", age=40, gender="male")
    
    # Add menus to the session
    session.add_all([a1, a2, a3])
    session.commit()

    print("Data inserted")

if __name__ == '__main__':
    create_tables()
    insert_data()
