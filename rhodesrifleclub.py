from flask import Flask
from flask import jsonify
from flask.ext.sqlalchemy import SQLAlchemy
from member import Member

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rhodesrifleclub.db'
db = SQLAlchemy(application)

@application.route("/members.json")
def members():
    members = Member.query.all()
    return jsonify(users = [member.username for member in members])

@application.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

if __name__ == "__main__":
    application.run(debug=True, host='0.0.0.0')
