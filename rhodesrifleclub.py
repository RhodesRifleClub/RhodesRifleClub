from flask import Flask
from flask import jsonify
from flask.ext.sqlalchemy import SQLAlchemy

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rhodesrifleclub.db'
db = SQLAlchemy(application)

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    first_name = db.Column(db.String(120))
    last_name = db.Column(db.String(120))

    def __init__(self, email, first_name, last_name):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return '%r %r' % self.first_name, self.last_name

@application.route("/members.json")
def members():
    members = Member.query.all()
    return jsonify(users = [member.username for member in members])

@application.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

if __name__ == "__main__":
    application.run(debug=True, host='0.0.0.0')
