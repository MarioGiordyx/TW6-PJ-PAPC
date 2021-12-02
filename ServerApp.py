from flask import Flask, render_template

app = Flask(__name__, template_folder='', static_folder='')


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__name__':
    app.run(debug=True)