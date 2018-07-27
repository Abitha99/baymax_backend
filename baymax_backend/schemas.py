from marshmallow import Schema, fields, post_load

from baymax_backend.models import User


class UserSchema(Schema):
    id = fields.Integer()
    first_name = fields.Str()
    last_name = fields.Str()
    email = fields.Email()
    phone = fields.Str()

    @post_load
    def make_user(self, data):
        return User(**data)
