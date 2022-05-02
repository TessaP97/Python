from ..config.mysqlconnection import connectToMySQL
from flask import flash
from ..models import user
from..models import band



class Band:
    def __init__(self, data):
        self.id = data['id']
        self.band_name = data['band_name']
        self.music_genre = data['music_genre']
        self.home_city = data['home_city']
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
        query = "SELECT * FROM bands"
        results = connectToMySQL("band_schema").query_db(query)
        all_bands = []
        for band_row in results:
            band_obj = cls(band_row)
            all_bands.append(band_obj)
        return all_bands

    @classmethod
    def get_all_users_bands(cls, data):
        query = "SELECT * FROM bands WHERE user_id = %(id)s"
        results = connectToMySQL("band_schema").query_db(query, data)

        return results


    @classmethod
    def get_by_id_2(cls, data):
        query = "SELECT * FROM users LEFT JOIN bands ON users.id = bands.user_id WHERE users.id = %(id)s;"

        results = connectToMySQL("band_schema").query_db(query, data)

        user = cls(results[0])
        
        if results[0]['bands.id'] != None:
            for row in results:
                row_data = {
                    "id": row['bands.id'],
                    "band_name": row['band_name'],
                    "music_genre": row['music_genre'],
                    "home_city": row['home_city'],
                    "created_at": row['bands.created_at'],
                    "updated_at": row['bands.updated_at'],
                    "user": user
                }

                user.bands.append(band.Band(row_data))

        return user

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM bands WHERE id = %(id)s"
        results = (connectToMySQL("band_schema").query_db(query, data))
        row_data = {
            "id": results[0]['id'],
            "band_name": results[0]['band_name'],
            "music_genre": results[0]['music_genre'],
            "home_city": results[0]['home_city'],
            "created_at": results[0]['created_at'],
            "updated_at": results[0]['updated_at'],
            "user_id": results[0]['user_id']
        }
        return cls(row_data)



    @classmethod
    def create(cls, data):
        query = "INSERT INTO bands (user_id, band_name, music_genre, home_city, created_at, updated_at) VALUES (%(user_id)s, %(band_name)s, %(music_genre)s, %(home_city)s, NOW(), NOW())"
        return connectToMySQL("band_schema").query_db(query,data)


    @classmethod
    def update(cls, data):
        query = "UPDATE bands SET band_name = %(band_name)s, music_genre = %(music_genre)s, home_city = %(home_city)s, updated_at = NOW() WHERE id = %(id)s"
        return connectToMySQL("band_schema").query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM bands WHERE id = %(id)s"
        return connectToMySQL("band_schema").query_db(query, data)

    @staticmethod
    def validate(post_data):
        is_valid = True

        if len(post_data['band_name']) < 1:
            flash("Band Name is required.")
            is_valid = False
        
        if len(post_data['music_genre']) < 1:
            flash("Music Genre is required.")
            is_valid = False
        
        if len(post_data['home_city']) < 1:
            flash("Home city is required.")
            is_valid = False

        return is_valid

