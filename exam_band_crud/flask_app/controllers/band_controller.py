from flask import render_template, request, session, redirect
from flask_app import app
from ..models.user import User
from flask_app.models.band import Band

@app.route("/dashboard")
def get_all_bands_controller():
    if "uuid" not in session:
        return redirect("/")
    all_bands = Band.get_all()
    print(all_bands)
    return render_template("dashboard.html", all_bands = all_bands, user = User.get_by_id({"id": session['uuid']}))

@app.route("/new/band")
def new_band():
    if "uuid" not in session:
        return redirect("/")
    all_bands = Band.get_all()
    return render_template("create_a_band.html", all_bands = all_bands ,user = User.get_by_id({"id": session['uuid']}))

@app.route("/new/band", methods = ['POST'])
def create_band():
    if not Band.validate(request.form):
        return redirect("/new/band")
    data = {
        "band_name": request.form['band_name'],
        "music_genre": request.form['music_genre'],
        "home_city": request.form['home_city'],
        "user_id": session['uuid']
    }
    Band.create(data)
    return redirect("/dashboard")


# @app.route("/mybands")
# def display_my_bands():
#     if "uuid" not in session:
#         return redirect("/")
#     return render_template("users_bands.html", band = Band.get_all_users_bands({"id": id}), user = User.get_by_id({"id": session['uuid']}))

@app.route("/mybands/<int:id>")
def display_my_bands(id):
    if "uuid" not in session:
        return redirect("/")
    
    return render_template(
        "users_bands.html",
        user = User.get_by_id({"id": session['uuid']}),
        all_bands = Band.get_all_users_bands({"id": session['uuid']})
    )


@app.route("/edit/<int:id>")
def edit_band(id):
    if "uuid" not in session:
        return redirect("/")
    
    return render_template("edit_band.html", band = Band.get_one({"id": id}), user = User.get_by_id({"id": session["uuid"]}))

@app.route("/edit/<int:id>", methods = ['POST'])
def update_band(id):
    if not Band.validate(request.form):
        return redirect(f"/edit/{id}")
    print(request.form)

    data = {
            "band_name": request.form['band_name'],
            "music_genre": request.form['music_genre'],
            "home_city": request.form['home_city'],
            "user_id": session['uuid'],
            "id": id
        }

    Band.update(data)
    return redirect("/dashboard")

@app.route("/band/<int:id>/delete")
def delete_band(id):
    Band.delete({"id": id})
    return redirect("/dashboard")
