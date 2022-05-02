from ..config.mysqlconnection import connectToMySQL
from flask import flash


class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made_on = data['date_made_on']
        self.under_30_min = data['under_30_min']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']



    # this displays all the recipes on the dashboard
    @classmethod
    def get_all_recipes(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL("recipe_schema").query_db(query)
        recipes = []
        for row in results:
            recipes.append(Recipe(row))

        return recipes



    # this creates a new recipe and inserts the recipe info into my table
    @classmethod
    def create_recipe(cls, data):
        print(data)
        query = "INSERT INTO recipes (name, description, instructions, date_made_on, under_30_min, created_at, updated_at, user_id) VALUES (%(name)s, %(description)s, %(instructions)s, %(date_made_on)s, %(under_30_min)s, NOW(), NOW() %(user_id)s);"
        recipe_id = connectToMySQL("recipe_schema").query_db(query, data)
        return recipe_id


    # this updates/edits my recipes
    @classmethod
    def edit_recipe(cls, data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, date_made_on = %(date_made_on)s, under_30_min = %(under_30_min)s, updated_at = NOW() WHERE id = %(id)s;"

        connectToMySQL("recipe_schema").query_db(query, data)

    @staticmethod
    def validate(post_data):
        is_valid = True

        if len(post_data['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        
        if len(post_data['description']) < 3:
            flash("description must be at least 3 characters.")
            is_valid = False

        if len(post_data['instructions']) < 3:
            flash("Instructions must be at least 3 characters.")
            is_valid = False

        return is_valid