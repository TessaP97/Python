from ..config.mysqlconnection import connectToMySQL
from .ninja_model import Ninja


class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # this displays all the dojos on my index.html page in a list 
    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL("dojo_ninja_schema").query_db(query)
        dojos = []
        for row in results:
            dojos.append(Dojo(row))
        return dojos

    # this creates a dojo location on the index.html page 
    @classmethod
    def create_dojo(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        dojo_id = connectToMySQL("dojo_ninja_schema").query_db(query, data)

        return dojo_id


    # this puts the ninjas on the dojo_show html page depending on the dojo location you choose from 
    @classmethod 
    def get_one_with_ninjas(cls, data):
        query = "SELECT * FROM dojos JOIN ninjas on dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL("dojo_ninja_schema").query_db(query, data)
        dojo = Dojo(results[0])
        dojo.ninjas = []
        for ninja in results:
            dojo.ninjas.append(Ninja(ninja))
        return dojo
