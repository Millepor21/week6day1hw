from flask import request
from flask.views import MethodView
from flask_smorest import abort
from sqlalchemy.exc import IntegrityError
from schemas import ReviewSchema, DeleteReview, UpdateReviewSchema
from . import bp
from .ReviewModel import ReviewModel
from db import reviews, movies

@bp.route('/reviews')
class ReviewList(MethodView):

    @bp.response(200, ReviewSchema(many = True))
    def get(self):
        return ReviewModel.query.all()

    @bp.arguments(ReviewSchema)
    @bp.response(201, ReviewSchema)
    def post(self, review_data):
        review = ReviewModel()
        review.from_dict(review_data)
        review.save()
        return review_data
    
    @bp.arguments(DeleteReview)
    def delete(self, review_data):
        review = ReviewModel.query.filter_by(username=review_data['username'],movie_id=review_data['movie_id']).first()
        if review:
            review.delete()
            return {'message':f'Review for movie_id {review_data["movie_id"]} by {review_data["username"]} deleted'}
        abort(400, message='Username or Movie_id invalid')

@bp.route('/reviews/<review_id>')
class Review(MethodView):

    @bp.response(200, ReviewSchema)
    def get(self, review_id):
        return ReviewModel.query.get_or_404(review_id, description='Review not found')
        
    @bp.arguments(UpdateReviewSchema)
    @bp.response(202, ReviewSchema)
    def put(self, review_data, review_id):
        review = ReviewModel.query.get_or_404(review_id, description='Review not found')
        if review:
            review.from_dict(review_data)
            review.save()