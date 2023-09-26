from flask import request
from uuid import uuid4

from app import app
from db import movies, reviews

@app.get('/movies')
def get_movies():
    return {'movies': movies}, 200

@app.get('/movies/<movie_id>')
def get_movie(movie_id):
    try:
        movie = movies[movie_id]
        return movie, 200
    except KeyError:
        return {'message': 'Movie not found'}, 400

@app.post('/movies')
def add_movie():
    movie_data = request.get_json()
    movies[uuid4().hex] = movie_data
    return movie_data, 201

@app.put('/movies/<movie_id>')
def update_movie(movie_id):
    movie_data = request.get_json()
    try:
        movie = movies[movie_id]
        movie['Title'] = movie_data['Title']
        return movie, 200
    except KeyError:
        return {'message': 'Movie not found'}, 400

@app.delete('/movies')
def delete_movie():
    movie_data = request.get_json()
    for i, movie in enumerate(movies):
        if movie["Title"] == movie_data["Title"]:
            movies.pop(i)
    return {'message':f'{movie_data["Title"]} deleted'}, 202

@app.get('/movies/<movie_id>/reviews')
def get_movie_reviews(movie_id):
    if movie_id not in movies:
        return {'message': 'Movie not found'}, 400
    movie_reviews = [review for review in reviews.values() if review['movie_id'] == movie_id]
    return movie_reviews, 200