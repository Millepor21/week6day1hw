from flask.views import MethodView
from flask_smorest import abort
from schemas import MovieSchema, DeleteMovie, UpdateMovieSchema
from . import bp
from .MovieModel import MovieModel

@bp.route('/movies')
class MovieList(MethodView):
    
    @bp.response(200, MovieSchema(many = True))
    def get(self):
        return MovieModel.query.all()
    
    @bp.arguments(MovieSchema)
    @bp.response(201, MovieSchema)
    def post(self, movie_data):
        movie = MovieModel()
        movie.from_dict(movie_data)
        movie.save()
        return movie_data

    @bp.arguments(DeleteMovie)
    def delete(self, movie_data):
        movie = MovieModel.query.filter_by(movie_id=movie_data['id'], title=movie_data['title']).first()
        if movie:
            movie.delete()
            return {'message':f'{movie_data["title"]} information deleted'}
        abort(400, message='Title or Movie_id invalid')

@bp.route('/movies/<movie_id>')
class Movie(MethodView):

    @bp.response(200, MovieSchema)
    def get(self, movie_id):
        return MovieModel.query.get_or_404(movie_id, description='Movie not found')
    
    @bp.arguments(UpdateMovieSchema)
    @bp.response(202, MovieSchema)
    def put(self, movie_data, movie_id):
        movie = MovieModel.query.get_or_404(movie_id, description='Movie not found')
        if movie:
            movie.from_dict(movie_data)
            movie.save()