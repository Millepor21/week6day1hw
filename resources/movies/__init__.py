from flask_smorest import Blueprint

bp = Blueprint('movies',__name__)

from . import routes