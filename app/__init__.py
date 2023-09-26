from flask import Flask
from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from Config import Config
app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)

from resources.reviews import bp as review_bp
api.register_blueprint(review_bp)
from resources.movies import bp as movie_bp
api.register_blueprint(movie_bp)

from resources.movies import routes
from resources.reviews import routes

from resources.reviews.ReviewModel import ReviewModel