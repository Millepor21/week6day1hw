from marshmallow import Schema, fields

class ReviewSchema(Schema):
    id = fields.Int(dump_only = True)
    username = fields.Str(required = True)
    stars = fields.Str(required = True)
    body = fields.Str(required = True)
    movie_id = fields.Str(required = True)

class MovieSchema(Schema):
    id = fields.Int(dump_only = True)
    title = fields.Str(required = True)
    description = fields.Str(required = True)
    streamed_on = fields.Str(required = False)
    rating = fields.Str(required = True)
    username = fields.Str(required = True)

class MovieReviewNested(Schema):
    reviews = fields.List(fields.Nested(ReviewSchema), dump_only = True)
    movie = fields.List(fields.Nested(MovieSchema), dump_only = True)

class UpdateReviewSchema(Schema):
    username = fields.Str(required = True)
    stars = fields.Str()
    body = fields.Str()
    movie_id = fields.Str()

class DeleteReview(Schema):
    username = fields.Str(required = True)
    movie_id = fields.Int(required = True)

class DeleteMovie(Schema):
    title = fields.Str(required = True)
    movie_id = fields.Int(required = True)

class UpdateMovieSchema(Schema):
    id = fields.Int(required=True)
    title = fields.Str()
    description = fields.Str()
    streamed_on = fields.Str()
    rating = fields.Str()
    username = fields.Str(required=True)
    
class UserSchema(Schema):
  id = fields.Str(dump_only = True)
  username = fields.Str(required = True)
  email = fields.Str(required = True)
  password = fields.Str(required = True, load_only = True)
  first_name = fields.Str()
  last_name = fields.Str()
  
class UserSchemaNested(UserSchema):
  posts = fields.List(fields.Nested(ReviewSchema), dump_only=True)
  followed = fields.List(fields.Nested(UserSchema), dump_only=True)

class UpdateUserSchema(Schema):
  username = fields.Str()
  email = fields.Str()
  password = fields.Str(required = True, load_only = True)
  new_password = fields.Str()
  first_name = fields.Str()
  last_name = fields.Str()

class AuthUserSchema(Schema):
  username = fields.Str()
  email = fields.Str()
  password = fields.Str(required = True, load_only = True)