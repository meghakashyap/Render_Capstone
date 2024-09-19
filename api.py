import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS
from auth import requires_auth, AuthError
from models import db, Actor,Movie, setup_db

# from models import db, db_drop_and_create_all, setup_db, 

app = Flask(__name__)
setup_db(app)
CORS(app, resources={r"/*": {"origins": "*"}})



@app.route("/")
def home():
    return  jsonify({
        "Hey": "welcome to Capstone !"
    })
    
@app.route("/home")
def home_page():
    try:
        movies = Movie.query.all()
        return jsonify({
            "success": True,
            "movies": [{
                'id': r.id,
                'title': r.title,
                'release_date': r.release_date,
            } for r in movies]
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": "An error occurred while fetching the movie details"
        }), 422

# This enpoint will show all the actors
@app.route("/actors", methods=["GET"])
@requires_auth('get:actor')
def getActor(payload):
    try:
        actors = Actor.query.all()
        actors_formatted = [actor.format() for actor in actors]
        return jsonify({
            "success":True, "actor":actors_formatted
        },200)
    except Exception as e:
        print(f"Error fetching actors {e}")
        abort(500)

# This enpoint will show all the movies
@app.route("/movies", methods=["GET"])
@requires_auth('get:movie')
def getMovie(payload):
    try:
        movies = Movie.query.all()
        movies_formatted = [movie.format() for movie in movies]
        
        return jsonify({
            "success":True, "movie":movies_formatted
        },200)
    except Exception as e:
        print(f"Error fetching movie: {e}")
        abort(500)



# This endpoint will add the actor
@app.route("/actors",methods=["POST"])
@requires_auth("post:actor")
def addActor(payload):
    body = request.get_json()
    
    if not body:
        abort(400, description=" Request doesn't contain required json body")
    
    if 'name' not in body:
        abort(400, description="Name is missing !")
    try:
        new_name = body.get("name")
        new_age = body.get("age")
        new_gender = body.get("gender")
        actor = Actor(name=new_name, age=new_age, gender=new_gender)
        actor.insert()
    
        
        return jsonify({
            "success": True, 
            "actor": actor.format()
        })

    except Exception as e:
        print(f"Error creating actor: {e}")
        abort(500, description="Acn error ocurred while creating the actor")
        
# This endpoint will add the movie
@app.route("/movies",methods=["POST"])
@requires_auth("post:movie")
def addMovie(payload):
    body = request.get_json()
    
    if not body:
        abort(400, description=" Request doesn't contain required json body")
    
    if 'title' not in body or 'release_date' not in body:
        abort(400, description="Title or release date  is missing !")
        
    try:
        movie = Movie(
            title = body.get('title'),
            release_date = body.get('release_date'),
            
        )
        movie.insert()
        
        return jsonify({
            "success": True, 
            "movie": movie.format()
        })
        
        
    except Exception as e:
        print(f"Error creating movie: {e}")
        abort(500, description="Acn error ocurred while creating the movie")
        

# This endpoint will update the actor detils
@app.route("/actors/<int:id>",methods=["PATCH"])
@requires_auth("patch:actor")
def updateActor(payload,id):
    body = request.get_json()
    actor = Actor.query.filter_by(id=id).one_or_none()
    
    if actor is None:
        abort(404)
    if "name" in body:
        actor.name = body.get("name")
    if "age" in body:
        actor.age = body.get("age")
    if "gender" in body:
        actor.gender = body.get("gender")

    try:
        actor.update()
    except Exception as e:
        print(e)
        abort(404)

    return jsonify({"success": True, "actor": [actor.format()]})


# This endpoint will update the movie detils
@app.route("/movies/<int:id>",methods=["PATCH"])
@requires_auth("patch:movie")
def updateMovie(payload,id):
    body = request.get_json()
    movie = Movie.query.filter_by(id=id).one_or_none()
    
    if movie is None:
        abort(404)
    if "title" in body:
        movie.title = body.get("title")
    if "release_date" in body:
        movie.release_date = body.get("release_date")

    try:
        movie.update()
    except Exception as e:
        print(e)
        abort(404)

    return jsonify({"success": True, "movie": [movie.format()]})



# This endpoint will delete the actor from the lsit
@app.route("/actors/<int:id>",methods=["DELETE"])
@requires_auth("delete:actor")
def deleteActor(payload,id):
    actor = Actor.query.filter_by(id=id).one_or_none()
    if actor is None:
            abort(404)
    
    try:
        actor.delete()
        return jsonify({"success": True, "id": id})
    except Exception as e:
        print(e)
        abort(500)
        
# This endpoint will delete the movie  from the lsit
@app.route("/movies/<int:id>",methods=["DELETE"])
@requires_auth("delete:movie")
def deleteMovie(payload,id):
    movie = Movie.query.filter_by(id=id).one_or_none()
    if movie is None:
            abort(404)
    
    try:
        movie.delete()
        return jsonify({"success": True, "id": id})
    except Exception as e:
        print(e)
        abort(500)
        

# Error Handling
@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422

@app.errorhandler(400)
def bad_request(error):
        return ( 
            jsonify({
            "success":False,
            "error": 400,
            "message":"Bad Request",
        }),400,
        )
        
@app.errorhandler(401)
def not_found(error):
    return (
        jsonify({
            "success": False, 
            "error": 401,
            "message": "Not authorized"
            }),401,
    )        

@app.errorhandler(404)
def not_found(error):
        return ( 
            jsonify({
            "success":False,
            "error": 404,
            "message":"Not Found",
        }),404,
        )
        
@app.errorhandler(500)
def internal_server_error(error):
    return ( 
        jsonify({
        "success":False,
        "error": 500,
        "message":"Internal Server Error ",
    }),500,
    )       
    
    
@app.errorhandler(AuthError)
def auth_error(e):
    return (
        jsonify({
            "success": False,
            "error": e.status_code, 
            "message": e.error}),
        e.status_code,
    )
    
if __name__ == "__main__":
    app.run( debug=True)
