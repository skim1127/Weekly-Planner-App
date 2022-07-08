from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Event(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key = True)
    event_start_date = db.Column(db.DateTime)
    event_end_date = db.Column(db.DateTime)
    event_name = db.Column(db.String(100))