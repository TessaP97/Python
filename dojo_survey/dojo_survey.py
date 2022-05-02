from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def survey():
    return render_template("index.html")

@app.route('/result', methods = ["POST"])
def result():
    print(request.form)
    print(request.form['your_name'])
    print(request.form['campus'])
    print(request.form['favorite_language'])
    print(request.form['comments'])

    return render_template(
        "submitted_info.html",
        your_name = request.form['your_name'],
        campus = request.form['campus'],
        favorite_language = request.form['favorite_language'],
        comments = request.form['comments']
    )

if __name__ == "__main__":
    app.run(debug = True)