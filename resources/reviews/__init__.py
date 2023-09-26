from flask_smorest import Blueprint

bp = Blueprint('reviews',__name__,description='Ops on reviews')

from . import routes