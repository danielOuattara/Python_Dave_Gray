from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
api = Api(app)

# UserModel definition


class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f'User(name = {self.name}, email = {self.email})'

# Custom validation function for non-empty strings


def non_empty_string(value):
    if not value.strip():
        raise ValueError("Value cannot be empty")
    return value


# Request parser setup
user_args = reqparse.RequestParser()
user_args.add_argument('name', type=non_empty_string,
                       required=True, help='Name cannot be blank or empty')
user_args.add_argument('email', type=non_empty_string,
                       required=True, help='Email cannot be blank or empty')

# Response field definitions
userFields = {
    'id': fields.Integer,
    'name': fields.String,
    'email': fields.String,
}

# Users resource


class Users(Resource):
    @marshal_with(userFields)
    def get(self):
        users = UserModel.query.all()
        return users

    @marshal_with(userFields)
    def post(self):
        args = user_args.parse_args()
        user = UserModel(name=args['name'], email=args['email'])
        db.session.add(user)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return {'message': 'Email or name already exists'}, 400
        return user, 201

# User resource


class User(Resource):
    @marshal_with(userFields)
    def get(self, id):
        user = UserModel.query.get(id)
        if not user:
            abort(404, message="User not found")
        return user

    @marshal_with(userFields)
    def patch(self, id):
        user = UserModel.query.get(id)
        if not user:
            abort(404, message="User not found")
        args = user_args.parse_args()
        if args['name']:
            user.name = args['name']
        if args['email']:
            user.email = args['email']
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return {'message': 'Email or name already exists'}, 400
        return user

    @marshal_with(userFields)
    def delete(self, id):
        user = UserModel.query.get(id)
        if not user:
            abort(404, message="User not found")
        db.session.delete(user)
        db.session.commit()
        return '', 204


# Adding resources to the API
api.add_resource(Users, '/api/users/')
api.add_resource(User, '/api/users/<int:id>')


@app.route('/')
def home():
    return '<h1>Flask Rest API</h1>'


if __name__ == '__main__':
    app.run(debug=True)
