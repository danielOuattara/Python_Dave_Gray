from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)

# Configuring the SQLite database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
api = Api(app)

# User model representing the database table


class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f'User(name = {self.name}, email = {self.email})'

# Custom validation function to check for non-empty strings


def non_empty_string(value):
    if not value.strip():  # Checks if the value is empty after stripping any surrounding whitespace
        raise ValueError("Value cannot be empty")
    return value


# Request parser to validate input data
user_args = reqparse.RequestParser()
# Adding argument for 'name' with custom validation
user_args.add_argument('name', type=non_empty_string,
                       required=True, help='Name cannot be blank or empty')
# Adding argument for 'email' with custom validation
user_args.add_argument('email', type=non_empty_string,
                       required=True, help='Email cannot be blank or empty')

# Fields to be included in the JSON response
userFields = {
    'id': fields.Integer,
    'name': fields.String,
    'email': fields.String,
}

# Resource for handling user-related requests


class Users(Resource):
    @marshal_with(userFields)
    def get(self):
        users = UserModel.query.all()
        return users

    @marshal_with(userFields)
    def post(self):
        args = user_args.parse_args()  # Parse and validate input arguments
        user = UserModel(name=args['name'], email=args['email'])
        db.session.add(user)
        try:
            db.session.commit()  # Try to commit the new user to the database
        # Catch any IntegrityError (e.g., duplicate entries)
        except IntegrityError:
            db.session.rollback()  # Roll back the session in case of error
            return {'message': 'Email or name already exists'}, 400
        users = UserModel.query.all()
        return users, 201


# Adding the Users resource to the API
api.add_resource(Users, '/api/users/')


@app.route('/')
def home():
    return '<h1>Flask Rest API</h1>'


if __name__ == '__main__':
    app.run(debug=True)
