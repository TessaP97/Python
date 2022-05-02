from flask import render_template, request, session, redirect

from users_crud_app import app
from ..models.user import User


@app.route("/")
def index():
    user_table = User.get_all_users()

    return render_template("index.html", all_users = user_table)


@app.route("/users/new")
def new_user_form():
    return render_template("new_user.html")


@app.route("/users/create", methods = ["POST"])
def create_user():
    print(request.form)
    User.create(request.form)

    return redirect("/")

@app.route("/users/<int:user_id>")
def show_user(user_id):
    peachy = User.display_user({'id': user_id})

    return render_template("show_user.html", user = peachy)


@app.route("/users/<int:user_id>/delete")
def delete_user(user_id):
    User.delete({'id': user_id})

    return redirect("/")


@app.route("/users/<int:user_id>/edit")
def edit_user_form(user_id):
    return render_template("edit_user.html", user = User.display_user({'id': user_id}))


@app.route("/users/<int:user_id>/update", methods = ['POST'])
def update_user(user_id):
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "id": user_id
    }
    User.update(data)
    return redirect(f"/users/{user_id}")
