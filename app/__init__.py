from flask import Flask

app = Flask(__name__)

from resources.movies import routes
from resources.reviews import routes