import os
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from extensions import db
from models.movie import MovieModel
from schemas import MovieSchema, UpdateMovieSchema
from sqlalchemy.exc import SQLAlchemyError, IntegrityError


blp = Blueprint(
    "movies",
    __name__,
    url_prefix=f'{os.getenv("BASE_PATH")}{os.getenv("MOVIES_URL_PREFIX")}',
    description="Movies Endpoint",
)


@blp.route("/")
class Movie(MethodView):
    @blp.response(200, MovieSchema(many=True))
    def get(self):
        movies = MovieModel.query.all()
        return movies

    @blp.arguments(MovieSchema)
    @blp.response(201, MovieSchema)
    def post(self, movie_data):
        movie = MovieModel(**movie_data)
        try:
            db.session.add(movie)
            db.session.commit()
        except IntegrityError:
            abort(400, message="Movie's title already exists")
        except SQLAlchemyError:
            abort(500, message="Error ocurred while insert movie.")
        return movie


@blp.route("/<movie_id>")
class MovieById(MethodView):
    @blp.response(200, MovieSchema)
    def get(self, movie_id):
        movie = MovieModel.query.get_or_404(movie_id)
        return movie

    @blp.arguments(UpdateMovieSchema)
    @blp.response(200, MovieSchema)
    def put(self, movie_data, movie_id):
        movie = MovieModel.query.get_or_404(movie_id)

        for key, value in movie_data.items():
            setattr(movie, key, value)
        db.session.commit()
        return movie

    @blp.response(200)
    def delete(self, movie_id):
        movie = MovieModel.query.get_or_404(movie_id)
        db.session.delete(movie)
        db.session.commit()
        return {"message": "The movie was deleted."}
