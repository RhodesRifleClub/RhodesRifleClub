from flask import Flask
from flask import jsonify
from flask.ext.sqlalchemy import SQLAlchemy

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rhodesrifleclub.db'
db = SQLAlchemy(application)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

@application.route("/users")
def users():
    users = User.query.all()
    return jsonify(users = [user.username for user in users])

@application.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

if __name__ == "__main__":
    application.run(debug=True, host='0.0.0.0')
