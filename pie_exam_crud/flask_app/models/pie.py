from ..config.mysqlconnection import connectToMySQL
from flask import flash
from ..models import user




class Pypie:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.filling = data['filling']
        self.crust = data['crust']
        self.votes = data['votes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @property
    def get_user(self):
        info = {
            "id": self.user_id
        }
        return user.User.get_by_id(info)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM pypies"
        results = connectToMySQL("pie_schema").query_db(query)
        all_pypies = []
        for pypie_row in results:
            pypie_obj = cls(pypie_row)
            all_pypies.append(pypie_obj)
        return all_pypies

    @classmethod
    def get_all_users_pypies(cls, data):
        query = "SELECT * FROM pypies WHERE user_id = %(id)s"
        results = connectToMySQL("pie_schema").query_db(query, data)

        return results

# @classmethod
#  def increase_votes():
#    query = "UPDATE pypies SET votes = votes + 1 WHERE id = %(id)s;"
#     results = connectToMySQL("pie_schema").query_db(query)
#     return results


    @classmethod
    def get_by_id_2(cls, data):
        query = "SELECT * FROM users LEFT JOIN pypies ON users.id = pypies.user_id WHERE users.id = %(id)s;"

        results = connectToMySQL("pie_schema").query_db(query, data)

        user = cls(results[0])
        
        if results[0]['pypies.id'] != None:
            for row in results:
                row_data = {
                    "id": row['pypies.id'],
                    "name": row['name'],
                    "filling": row['filling'],
                    "crust": row['crust'],
                    "votes": row['votes'],
                    "created_at": row['pypies.created_at'],
                    "updated_at": row['pypies.updated_at'],
                    "user": user
                }

                user.pypies.append(Pypie(row_data))

        return user

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM pypies WHERE id = %(id)s"
        results = (connectToMySQL("pie_schema").query_db(query, data))
        row_data = {
            "id": results[0]['id'],
            "name": results[0]['name'],
            "filling": results[0]['filling'],
            "crust": results[0]['crust'],
            "votes": results[0]['votes'],
            "created_at": results[0]['created_at'],
            "updated_at": results[0]['updated_at'],
            "user_id": results[0]['user_id']
        }
        return cls(row_data)



    @classmethod
    def create(cls, data):
        query = "INSERT INTO pypies (user_id, name, filling, crust, created_at, updated_at) VALUES (%(user_id)s, %(name)s, %(filling)s, %(crust)s, NOW(), NOW())"
        return connectToMySQL("pie_schema").query_db(query,data)


    @classmethod
    def update(cls, data):
        query = "UPDATE pypies SET name = %(name)s, filling = %(filling)s, crust = %(crust)s, updated_at = NOW() WHERE id = %(id)s"
        return connectToMySQL("pie_schema").query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM pypies WHERE id = %(id)s"
        return connectToMySQL("pie_schema").query_db(query, data)

    @staticmethod
    def validate(post_data):
        is_valid = True

        if len(post_data['name']) < 1:
            flash("Name is required.")
            is_valid = False
        
        if len(post_data['filling']) < 1:
            flash("Filling is required.")
            is_valid = False
        
        if len(post_data['crust']) < 1:
            flash("Crust is required.")
            is_valid = False

        return is_valid

