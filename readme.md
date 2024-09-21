# CAPSTONE PROJECT - RENDER HOSTED

## Casting Agency  System

The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process

### Models:
Movies with attributes title and release date
Actors with attributes name, age and gender




### To test the project locally

Fork this project - https://github.com/meghakashyap/Render_Capstone/tree/master

Setup this project by runnning this command - pip install -r requirements.txt

Create database tables - python create-db-tables.py

Run the app - flask run --reload

Test the application after generating valid token with required permissions from auth0 and run - pytest test-app.py

There are three roles associated with this project
Roles:
# Casting Assistant
Can view actors and movies

# Casting Director
All permissions a Casting Assistant has and…
Add or delete an actor from the database
Modify actors or movies

# Executive Producer
All permissions a Casting Director has and…
Add or delete a movie from the database


Casting Director has all access 

### Render details

This applications is hosted in render url - https://render-capstone-un0i.onrender.com

### API Endpoints:

GET /actors and /movies
DELETE /actors/ and /movies/
POST /actors and /movies and
PATCH /actors/ and /movies/


GET /actors: Lists all actors
GET /movies: Lists all movies
POST /actors: Adds a new actor.
POST /movies: Adds a new movie.
PATCH /actors/<int:id>: Edit a  actor.
PATCH /movies/<int:id>: Edit a movie.
DELETE /actors/<int:id>: Deletes a specific actor
DELETE /movies/<int:id>: Deletes a specific movie




