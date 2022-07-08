# Import blueprint Class
from flask import Blueprint

# Instantiate blueprint
bp = Blueprint(
    'users',
    __name__,
    url_prefix='/users'
)

# Users Index Route
@bp.route('/')
def index():
    return 'This is the Users Index'