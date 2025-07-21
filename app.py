from flask import Flask
from config import Config
from extensions import db, api
from dotenv import load_dotenv
from resources.movies import blp as MoviesBlueprint


def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    api.init_app(app)

    with app.app_context():
        db.create_all()

    api.register_blueprint(MoviesBlueprint)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
