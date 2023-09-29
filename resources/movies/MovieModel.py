from app import db

class MovieModel(db.Model):

    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String, nullable = False)
    description = db.Column(db.String, nullable = False)
    streamed_on = db.Column(db.String, nullable = True)
    rating = db.Column(db.String, nullable = False)
    username = db.Column(db.String, nullable = False)

    def __repr__(self):
        return f'<Title: {self.title}>\n<description: {self.description}>\n<rating: {self.rating}>'
    
    def from_dict(self, dict):
        for k,v in dict.items():
            setattr(self, k, v)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()