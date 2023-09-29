from flask.views import MethodView
from flask_smorest import abort
from sqlalchemy.exc import IntegrityError
from schemas import ReviewSchema, UpdateReviewSchema, MovieSchema
from . import bp
from .ReviewModel import ReviewModel
from flask_jwt_extended import jwt_required, get_jwt_identity

@bp.route('/reviews')
class ReviewList(MethodView):

    @jwt_required()
    @bp.response(200, ReviewSchema(many = True))
    def get(self):
        return ReviewModel.query.all()

    @jwt_required()
    @bp.arguments(ReviewSchema)
    @bp.response(201, ReviewSchema)
    def post(self, review_data):
        user_id = get_jwt_identity()
        review = ReviewModel(**review_data, user_id = user_id)
        try:
            review.save()
            return review
        except IntegrityError:
            abort(400, message='Invalid user_id')

@bp.route('/reviews/<review_id>')
class Review(MethodView):

    @jwt_required()
    @bp.response(200, ReviewSchema)
    def get(self, review_id):
        r = ReviewModel.query.get(review_id)
        if r:
            return r
        abort(400, message='Invalis post_id')

    @jwt_required()
    @bp.arguments(UpdateReviewSchema)
    @bp.response(202, ReviewSchema)
    def put(self, review_data, review_id):
        r = ReviewModel.query.get(review_id)
        if r and review_data['body']:
            user_id = get_jwt_identity()
            if r.user_id == user_id:
                r.body = review_data['body']
                r.save()
                return r
            else:
                abort(401, message='Unauthorized')
        abort(400, message='Invalid review_data')

    @jwt_required()
    def delete(self, review_id):
        user_id = get_jwt_identity()
        r = ReviewModel.query.get(review_id)
        if r:
            if r.user_id == user_id:
                r.delete()
                return {'message':'Review deleted'}, 202
            abort(401, message='User doesn\'t have rights')
        abort(400, message='Invalid review_id')