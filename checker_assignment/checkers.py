from flask import Flask, render_template
app = Flask(__name__)

@app.route('/<int:num>')
def checker_board(num):
    return render_template("index.html", color = 'red', num = num)

@app.route('/<color>/<int:num>')
def checker_board_colors(color, num):
    return render_template("index.html", color = color, num = num)


if __name__ == "__main__":
    app.run(debug = True)
