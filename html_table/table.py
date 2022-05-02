from flask import Flask, render_template
app = Flask(__name__)

@app.route('/table')
def name_table():
    names = [
        {'first_name' : 'Michael', 'last_name' : 'Choi', 'full_name' : 'Michael Choi'},
        {'first_name' : 'John', 'last_name' : 'Supsupin', 'full_name' : 'John Supsupin'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen', 'full_name' : 'Mark Guillen'}
    ]
    
    return render_template("index.html", list = names)

if __name__ == "__main__":
    app.run(debug = True)
