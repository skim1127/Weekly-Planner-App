# import necessary modules
from flask import Flask
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

load_dotenv()

# FACTORY
def create_app():
    app = Flask(__name__)

    # Database config
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQLALCHEMY_DATABASE_URI")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Import Database Models
    from . import models
    models.db.init_app(app)
    migrate = Migrate(app, models.db)

    @app.route('/')
    def hello():
        return "Hello & Welcome to the Planner API"

    # register users blueprint
    from . import users
    app.register_blueprint(users.bp)

    return app
