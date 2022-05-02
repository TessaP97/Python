from flask import render_template, request, session, redirect
from flask_app import app
from ..models.user import User
from flask_app.models.pie import Pypie

@app.route("/pies")
def get_all_pies_controller():
    if "uuid" not in session:
        return redirect("/")
    all_pypies = Pypie.get_all()
    print(all_pypies)
    return render_template("pypie_derby.html", all_pypies = all_pypies, user = User.get_by_id({"id": session['uuid']}))


@app.route("/new/pie", methods = ['POST'])
def create_pypie():
    if not Pypie.validate(request.form):
        return redirect("/dashboard")
    data = {
        "name": request.form['name'],
        "filling": request.form['filling'],
        "crust": request.form['crust'],
        "user_id": session['uuid']
    }
    Pypie.create(data)
    return redirect("/dashboard")

@app.route("/dashboard")
def dashboard():
    if "uuid" not in session:
        return redirect("/")
    
    return render_template(
        "dashboard.html",
        user = User.get_by_id({"id": session['uuid']}), all_pypies = Pypie.get_all_users_pypies({"id": session['uuid']}))


@app.route("/dashboard/pies")
def display_my_pypies(id):
    if "uuid" not in session:
        return redirect("/")
    
    return redirect("/dashboard",
        user = User.get_by_id({"id": session['uuid']}),
        all_pypies = Pypie.get_all_users_pypies({"id": session['uuid']}))


@app.route("/edit/<int:id>")
def edit_pypie(id):
    if "uuid" not in session:
        return redirect("/")
    
    return render_template("edit_pypie.html", pypie = Pypie.get_one({"id": id}), user = User.get_by_id({"id": session["uuid"]}))

@app.route("/edit/<int:id>", methods = ['POST'])
def update_pypie(id):
    if not Pypie.validate(request.form):
        return redirect(f"/edit/{id}")
    print(request.form)

    data = {
            "name": request.form['name'],
            "filling": request.form['filling'],
            "crust": request.form['crust'],
            "user_id": session['uuid'],
            "id": id
        }

    Pypie.update(data)
    return redirect("/dashboard")

@app.route("/pypie/<int:id>/delete")
def delete_pypie(id):
    Pypie.delete({"id": id})
    return redirect("/dashboard")



@app.route("/show/<int:id>")
def vote_pies(id):
    if "uuid" not in session:
        return redirect("/")

    return render_template("votes.html", pypie = Pypie.get_one({"id": id}), user = User.get_by_id({"id": session["uuid"]}))


@app.route("/vote")
def vote_button():
    if "uuid" not in session:
        return redirect("/")
    return redirect("/pies")