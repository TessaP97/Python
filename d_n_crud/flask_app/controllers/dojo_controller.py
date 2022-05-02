from flask import render_template, request, session, redirect
from flask_app import app
from ..models.dojo_model import Dojo 

# display routes 

@app.route("/dojos/")
def index():
    dojos = Dojo.get_all_dojos()
    return render_template('index.html', dojos = dojos)


@app.route("/dojos/<int:dojo_id>")
def show_dojo(dojo_id):
    this_dojo = Dojo.get_one_with_ninjas({'id': dojo_id})
    return render_template("dojo_show.html", this_dojo = this_dojo)


# action routes 

@app.route("/dojos/create", methods = ["POST"])
def create_dojo():
    Dojo.create_dojo(request.form)
    return redirect("/dojos")






