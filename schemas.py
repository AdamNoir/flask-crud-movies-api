from marshmallow import Schema, fields, validate


class MovieSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(
        required=True,
        validate=validate.Length(
            min=1, max=99, error="Title must be between 1 and 99 characters."
        ),
        error_messages={"error": "Movie Title is required"},
    )
    director = fields.Str(
        validate=validate.Length(
            min=1, max=99, error="Director must be between 1 and 99 characters."
        ),
        allow_none=True,
    )
    release_year = fields.Int()


class UpdateMovieSchema(Schema):
    title = fields.Str(
        validate=validate.Length(
            min=1, max=99, error="Title must be between 1 and 99 characters."
        )
    )
    director = fields.Str(
        validate=validate.Length(
            min=1, max=99, error="Director must be between 1 and 99 characters."
        )
    )
    release_year = fields.Int()
