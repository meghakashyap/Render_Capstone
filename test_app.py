
import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from dotenv import dotenv_values


from app import create_app
from models import setup_db, Movie, Actor, db
# from models import setup_db, Movie, Actor
from config import Testing


class CastingAgencyTestCase(unittest.TestCase):
    """This class represents the Casting Agency test cases"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        config = dotenv_values()
        # self.database_name = config["DBNAME"]
        self.database_name = "capstone"
        self.database_path = "postgresql://{}:{}@{}/{}".format(
            config["USERNAME"],
            config["PASSWORD"],
            config["HOSTNAME"] + ":" + config["PORT"],
            self.database_name,
        )

        # setup_db(self.app, self.database_path)

        # # binds the app to the current context
        # with self.app.app_context():
        #     # self.db = SQLAlchemy()sahi
        #     self.db.init_app(self.app)
        #     # create all tables
        #     self.db.create_all()
        # with self.app.app_context():
        #     self.db = self.app.extensions['sqlalchemy'].db
        self.app = create_app({
            "TESTING": True,
            "SQLALCHEMY_DATABASE_URI": self.database_path,
            "SQLALCHEMY_TRACK_MODIFICATIONS": False
        })
        
        self.client = self.app.test_client()


        # binds the app to the current context
        with self.app.app_context():
            db.create_all()
            
            
            
            

        # Test Data
        self.new_actor_one = {
                "name" : "Richard",
                "age" : 34,
                "gender": "Male"
            }

        self.new_actor_two = {
                "name" : "Diane",
                "age" : 55,
                "gender": "Female"
            }

        self.new_movie_one = {
                "title" : "Minion",
                "release_date" : "22-07-2024"
            }

        self.new_movie_two = {
                "title" : "Richard",
                "release_date" : "31-12-2025"
            }
        
        with self.app.app_context():
            # Add test data for actors
            actor_one = Actor(name="Richard", age=34, gender="Male")
            actor_two = Actor(name="Diane", age=55, gender="Female")
            db.session.add(actor_one)
            db.session.add(actor_two)
            db.session.commit()
            
            
        self.cast_assistant_header = {
            'Authorization': 'Bearer ' + Testing.cast_assistant_token}
        
        self.cast_director_header = {
            'Authorization': 'Bearer ' + Testing.cast_director_token}
        
        self.exec_producer_header = {
            'Authorization': 'Bearer ' + Testing.exec_producer_token}

        


        
    def tearDown(self):
        """Executed after reach test"""
        pass
    
    
    def test(self):
        response = self.client.get('/home') 
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        print(data)
        try:
            data = json.loads(response.data)
        except json.JSONDecodeError as e:
            self.fail(f"Failed to decode JSON response: {e}")
        self.assertEqual(data["success"], True)
    
    # def test_home(self):
    #     res = self.client.get("/")
    #     print(res.status_code)
    #     print(res.data)
    #     try:
    #         data = json.loads(res.data)
    #     except json.JSONDecodeError as e:
    #         self.fail(f"Failed to decode JSON response: {e}")
    #     self.assertEqual(data["success"], True)
    
   
        
    # def test_get_restaurants_list_without_auth0(self):
    #     response = self.client.get('/home')
    #     print(response.status_code)
    #     print(response.data)
    #     self.assertEqual(response.status_code, 200)



    # Test Cases for Casting Assistant
    def test_get_actors_cast_assistant(self):
        res = self.client.get("/actors", headers=self.cast_assistant_header)
        print(res.status_code)
        print(res.data)
        try:
            data = json.loads(res.data)
        except json.JSONDecodeError as e:
            self.fail(f"Failed to decode JSON response: {e}")
        self.assertEqual(data["success"], True)
    
    def test_get_movies_cast_assistant(self):
        res = self.client.get("/movies", headers=self.cast_assistant_header)
        print(res.status_code)
        print(res.data)
        try:
            data = json.loads(res.data)
        except json.JSONDecodeError as e:
            self.fail(f"Failed to decode JSON response: {e}")
        self.assertEqual(data["success"], True)

    # def test_add_actor_cast_assistant(self):
        res = self.client.post("/actors", headers=self.cast_assistant_header, json=self.new_actor_one)
        print(res.status_code)
        print(res.data)
        try:
            data = json.loads(res.data)
        except json.JSONDecodeError as e:
            self.fail(f"Failed to decode JSON response: {e}")
        self.assertEqual(data["success"], True)

    def test_add_movie_cast_assistant(self):
        res = self.client.post("/movies", headers=self.cast_assistant_header, json=self.new_movie_one)
        print(res.status_code)
        print(res.data)
        try:
            data = json.loads(res.data)
        except json.JSONDecodeError as e:
            self.fail(f"Failed to decode JSON response: {e}")
        self.assertEqual(data["success"], True)

    def test_update_actor_cast_assistant(self):
        res = self.client.patch("/actors/1", headers=self.cast_assistant_header, json=self.new_actor_two)
        print(res.status_code)
        print(res.data)
        try:
            data = json.loads(res.data)
        except json.JSONDecodeError as e:
            self.fail(f"Failed to decode JSON response: {e}")
        self.assertEqual(data["success"], True)

    def test_update_movie_cast_assistant(self):
        res = self.client.patch("/movies/3", headers=self.cast_assistant_header, json=self.new_movie_two)
        print(res.status_code)
        print(res.data)
        try:
            data = json.loads(res.data)
        except json.JSONDecodeError as e:
            self.fail(f"Failed to decode JSON response: {e}")
        self.assertEqual(data["success"], True)

    def test_delete_actor_cast_assistant(self):
        res = self.client.delete("/actors/5", headers=self.cast_assistant_header)
        print(res.status_code)
        print(res.data)
        try:
            data = json.loads(res.data)
        except json.JSONDecodeError as e:
            self.fail(f"Failed to decode JSON response: {e}")
        self.assertEqual(data["success"], True)

    def test_delete_movie_cast_assistant(self):
        res = self.client.patch("/movies/3", headers=self.cast_assistant_header)
        print(res.status_code)
        print(res.data)
        try:
            data = json.loads(res.data)
        except json.JSONDecodeError as e:
            self.fail(f"Failed to decode JSON response: {e}")
        self.assertEqual(data["success"], True)


    # Test Cases for Casting Director
        
    def test_get_actors_cast_director(self):
        res = self.client.get("/actors", headers=self.cast_director_header)
        print(res.status_code)
        print(res.data)
        try:
            data = json.loads(res.data)
        except json.JSONDecodeError as e:
            self.fail(f"Failed to decode JSON response: {e}")
        self.assertEqual(data["success"], True)
    
    def test_get_movies_cast_director(self):
        res = self.client.get("/movies", headers=self.cast_director_header)
        print(res.status_code)
        print(res.data)
        try:
            data = json.loads(res.data)
        except json.JSONDecodeError as e:
            self.fail(f"Failed to decode JSON response: {e}")
        self.assertEqual(data["success"], True)

    def test_add_actor_cast_director(self):
        res = self.client.post("/actors", headers=self.cast_director_header, json=self.new_actor_one)
        print(res.status_code)
        print(res.data)
        try:
            data = json.loads(res.data)
        except json.JSONDecodeError as e:
            self.fail(f"Failed to decode JSON response: {e}")
        self.assertEqual(data["success"], True)
        return data["actors"][0]["id"]

    def test_add_movie_cast_director(self):
        res = self.client.post("/movies", headers=self.cast_director_header, json=self.new_movie_one)
        print(res.status_code)
        print(res.data)
        try:
            data = json.loads(res.data)
        except json.JSONDecodeError as e:
            self.fail(f"Failed to decode JSON response: {e}")
        self.assertEqual(data["success"], True)

    def test_update_actor_cast_director(self):
        res = self.client.patch("/actors/2", headers=self.cast_director_header, json=self.new_actor_two)
        print(res.status_code)
        print(res.data)
        try:
            data = json.loads(res.data)
        except json.JSONDecodeError as e:
            self.fail(f"Failed to decode JSON response: {e}")
        self.assertEqual(data["success"], True)
        

    def test_update_movie_cast_director(self):
        res = self.client.patch("/movies/3", headers=self.cast_director_header, json=self.new_movie_two)
        print(res.status_code)
        print(res.data)
        try:
            data = json.loads(res.data)
        except json.JSONDecodeError as e:
            self.fail(f"Failed to decode JSON response: {e}")
        self.assertEqual(data["success"], True)


    def test_delete_actor_cast_director(self):
        actor_id = self.test_add_actor_cast_director()
        # print('actor id: ', actor_id)
        res = self.client.delete("/actors/" + str(actor_id), headers=self.cast_director_header)
        # print('res: ', res)
        print(res.status_code)
        print(res.data)
        try:
            data = json.loads(res.data)
        except json.JSONDecodeError as e:
            self.fail(f"Failed to decode JSON response: {e}")
        self.assertEqual(data["success"], True)
        

    def test_delete_movie_cast_director(self):
        res = self.client.delete("/movies/3", headers=self.cast_director_header)
        print(res.status_code)
        print(res.data)
        try:
            data = json.loads(res.data)
        except json.JSONDecodeError as e:
            self.fail(f"Failed to decode JSON response: {e}")
        self.assertEqual(data["success"], True)


    # Test Cases for Executive Producer
        
    def test_get_actors_exec_producer(self):
        res = self.client.get("/actors", headers=self.exec_producer_header)
        print(res.status_code)
        print(res.data)
        try:
            data = json.loads(res.data)
        except json.JSONDecodeError as e:
            self.fail(f"Failed to decode JSON response: {e}")
        self.assertEqual(data["success"], True)
    
    def test_get_movies_exec_producer(self):
        res = self.client.get("/movies", headers=self.exec_producer_header)
        print(res.status_code)
        print(res.data)
        try:
            data = json.loads(res.data)
        except json.JSONDecodeError as e:
            self.fail(f"Failed to decode JSON response: {e}")
        self.assertEqual(data["success"], True)

    def test_add_actor_exec_producer(self):
        res = self.client.post("/actors", headers=self.exec_producer_header, json=self.new_actor_one)
        print(res.status_code)
        print(res.data)
        try:
            data = json.loads(res.data)
        except json.JSONDecodeError as e:
            self.fail(f"Failed to decode JSON response: {e}")
        self.assertEqual(data["success"], True)
        return data["actors"][0]["id"]

    def test_add_movie_exec_producer(self):
        res = self.client.post("/movies", headers=self.exec_producer_header, json=self.new_movie_one)

        print(res.status_code)
        print(res.data)
        try:
            data = json.loads(res.data)
        except json.JSONDecodeError as e:
            self.fail(f"Failed to decode JSON response: {e}")
        self.assertEqual(data["success"], True)

    def test_update_actor_exec_producer(self):
        res = self.client.patch("/actors/2", headers=self.exec_producer_header, json=self.new_actor_two)
        print(res.status_code)
        print(res.data)
        try:
            data = json.loads(res.data)
        except json.JSONDecodeError as e:
            self.fail(f"Failed to decode JSON response: {e}")
        self.assertEqual(data["success"], True)

    def test_update_movie_exec_producer(self):
        res = self.client.patch("/movies/3", headers=self.exec_producer_header, json=self.new_movie_two)
        print(res.status_code)
        print(res.data)
        try:
            data = json.loads(res.data)
        except json.JSONDecodeError as e:
            self.fail(f"Failed to decode JSON response: {e}")
        self.assertEqual(data["success"], True)

    def test_delete_actor_exec_producer(self):
        actor_id = self.test_add_actor_cast_director()
        res = self.client.delete("/actors/" + str(actor_id), headers=self.exec_producer_header)
        print(res.status_code)
        print(res.data)
        try:
            data = json.loads(res.data)
        except json.JSONDecodeError as e:
            self.fail(f"Failed to decode JSON response: {e}")
        self.assertEqual(data["success"], True)

    def test_delete_movie_exec_producer(self):
        movie_id = self.test_add_movie_exec_producer
        res = self.client().delete("/movies/" + str(movie_id), headers=self.exec_producer_header)
        print(res.status_code)
        print(res.data)
        try:
            data = json.loads(res.data)
        except json.JSONDecodeError as e:
            self.fail(f"Failed to decode JSON response: {e}")
        self.assertEqual(data["success"], True)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()