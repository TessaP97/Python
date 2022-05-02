from flask import render_template, request, session, redirect
from flask_bcrypt import Bcrypt

from flask_app import app

from ..models.recipe_model import Recipe

bcrypt = Bcrypt(app) #instantiating the Bcrypt class passing the flask app 


# gets all recipes and puts them in the table on the dashboard page after loggin in .. 
@app.route("/dashboard")
def get_all_recipes_controller():
    recipes = Recipe.get_all_recipes()
    return render_template('dashboard.html', recipes = recipes)


# this function takes you from the dashboard to the add/create recipe page
@app.route("/recipes/new")
def dashboard_to_add_recipe_page():
    return render_template("add_recipe.html")

# this route creates/adds a new recipe for the user joining by the foregin key 

@app.route("/recipes/new", methods = ["POST"])
def create_recipe_controller():
    Recipe.create_recipe(request.form)

    return redirect("/recipes/new")


# this route updates my recipes on my edit recipe form 
@app.route("/recipes/edit/<int:recipe_id>/", methods = ['POST'])
def edit_recipe_controller(recipe_id):
    data = {
        "name": request.form['name'],
        "under_30_min": request.form['under_30_min'],
        "description": request.form['description'],
        "instructions": request.form['instructions'],
        "date_made_on": request.form['date_made_on'],
        "id": recipe_id
    }
    Recipe.update(data)
    return redirect("/dashboard")

