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
    text = db.Column(db.String(100), default="text")
    deadline = db.Column(db.Integer, default=1)
    owner_id = db.Column(db.Integer, db.ForeignKey("homeworkResult.id"))


class HomeworkResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    solution = db.Column(db.String(100), default="solution")
    author = db.Column(db.String(100), default="author")
    created = db.Column(db.String(100), default="created")
    homework = db.relationship("Homework", backref="owner", lazy="dynamic")


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), default="first_name")
    last_name = db.Column(db.String(100), default="last_name")


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), default="first_name")
    last_name = db.Column(db.String(100), default="last_name")


if __name__ == "__main__":
    manager.run()