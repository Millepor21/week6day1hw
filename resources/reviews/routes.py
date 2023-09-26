from flask import request
from uuid import uuid4

from app import app

from db import reviews

@app.get('/reviews')
def get_reviews():
    return {'reviews': reviews}, 200

@app.get('/reviews/<review_id>')
def get_review(review_id):
    try:
        review = reviews[review_id]
        return review, 200
    except KeyError:
        return {'message': 'Review not found'}, 400

@app.post('/reviews')
def create_review():
    review_data = request.get_json()
    reviews[uuid4().hex] = review_data
    return review_data, 201

@app.put('/reviews/<review_id>')
def edit_review(review_id):
    review_data = request.get_json()
    if review_id in reviews:
        review = reviews[review_id]
        review["body"] = review_data["body"]
        return review, 200
    return {"message": 'Review not found'}, 400


@app.delete('/reviews/<review_id>')
def delete_review(review_id):
    try:
        deleted_review = reviews.pop(review_id)
        return {'message': f'{deleted_review["body"]} deleted'}, 202
    except KeyError:
        return {"message": 'Review not found'}, 400