from marshmallow import Schema, fields

class ReviewSchema(Schema):
    id = fields.Str(dump_only = True)
    username = fields.Str(required = True)
    stars = fields.Str(required = True)
    body = fields.Str(required = True)
    movie_id = fields.Str(required = True)

class UpdateReviewSchema(Schema):
    username = fields.Str(required = True)
    stars = fields.Str()
    body = fields.Str()
    movie_id = fields.Str()

class DeleteReview(Schema):
    username = fields.Str(required = True)
    movie_id = fields.Str(required = True)