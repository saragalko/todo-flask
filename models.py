from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300))
    is_complete = db.Column(db.Boolean)
