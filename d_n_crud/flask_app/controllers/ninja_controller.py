from flask import render_template, request, session, redirect

from flask_app import app
from ..models.ninja_model import Ninja
from ..models.dojo_model import Dojo # <---- imported Dojo model class to grab dictionary names 


# display routes


@app.route("/ninjas/")
def new_ninja():
    dojos = Dojo.get_all_dojos()
    return render_template("new_ninja.html", dojos = dojos)



# action routes 

@app.route("/ninjas/create", methods = ["POST"])
def create_ninja():
    Ninja.create_ninja(request.form)

    return redirect("/dojos")
