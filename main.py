from flask import Flask, send_from_directory, render_template
from random import choices

app = Flask(__name__)
app.secret_key = ''.join(choices("QWERTYUIOPASDFGHJKL:ZXCVBNM<>?!£$%^&*()_1234567890", k=20))
#Get rid of unesserary whitespace made by jinja
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

@app.route('/', methods=["GET"])
def home():
    return render_template("brief.html")

@app.route('/getcv', methods=["GET"])
def cv():
    return send_from_directory(app.root_path, 'mrcv')

@app.route('/projects', methods=["GET"])
def projects():
    return render_template("projects.html")

if __name__ == '__main__':
    app.run(debug = True)