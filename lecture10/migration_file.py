from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from app import db


from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config["TESTING"] = True
app.config["DEBUG"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)


class Homework(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(100))
    deadline = db.Column(db.Integer)
    owner_id = db.Column(db.Integer, db.ForeignKey("homeworkResult.id"))


class HomeworkResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    solution = db.Column(db.String(100))
    author = db.Column(db.String(100))
    created = db.Column(db.String(100))
    homework = db.relationship("Homework", backref="owner", lazy="dynamic")


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.Integer)


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.Integer)


if __name__ == "__main__":
    manager.run()