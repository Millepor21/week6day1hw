from datetime import datetime
from app import db

class ReviewModel(db.Model):

    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, nullable = False)
    stars = db.Column(db.String, nullable = False)
    body = db.Column(db.String, nullable = False)
    timestamp = db.Column(db.String, default = datetime.utcnow)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    

    def __repr__(self):
        return f'<Stars: {self.stars}>\n<Review: {self.body}>'
    
    def from_dict(self, dict):
        for k,v in dict.items():
            setattr(self, k, v)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()