from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    user_pw = db.Column(db.String)
    user_name = db.Column(db.String(100))
    events = db.relationship('Event', backref='users')
    checklists = db.relationship('Checklist', backref='users')

class Event(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key = True)
    event_start_date = db.Column(db.DateTime)
    event_end_date = db.Column(db.DateTime)
    event_name = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

class Checklist(db.Model):
    __tablename__ = 'checklists'

    id = db.Column(db.Integer, primary_key = True)
    checklist_name = db.Column(db.String(200))
    checklist_favorited = db.Column(db.Boolean)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    tasks = db.relationship('Task', backref='checklists')

class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key = True)
    task_name = db.Column(db.String(200))
    task_checked = db.Column(db.Boolean)
    checklist_id = db.Column(db.Integer, db.ForeignKey('checklists.id'))
