from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'davinci code'

@app.route('/')
def main_page():
    if "amount" not in session:
        session["amount"] = 1
    else:
        session["amount"] += 1
        
    return render_template("index.html")

@app.route('/destroy_session')
def destroy_amount():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug = True)