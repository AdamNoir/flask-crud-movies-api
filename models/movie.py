from extensions import db


class MovieModel(db.Model):
    __tablename__ = "movies"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    director = db.Column(db.String(100))
    release_year = db.Column(db.Integer)
