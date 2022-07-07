# CONFIG
from flask import Flask
app = Flask(__name__)

# INDEX ROUTE
@app.route('/')
def index():
    return 'Welcome to the Weekly Planner API'

# USERS INDEX ROUTE
@app.route('/users')
def users():
    return 'Users Index Route'