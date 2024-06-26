# Flask Ret API

## (00:00) Intro

## (00:12) Welcome

## (00:38) Tutorial Prerequisites

## (00:53) What is REST? What is an API?

## (03:07) REST API Diagram

## (04:27) Virtual Environment set up

## (07:19) Install Dependencies

```py
pip3 install Flask flask_restful flask_sqlalchemy
```

`requirements.txt`

```text
aniso8601==9.0.1
blinker==1.8.2
click==8.1.7
Flask==3.0.3
Flask-RESTful==0.3.10
Flask-SQLAlchemy==3.1.1
greenlet==3.0.3
itsdangerous==2.2.0
Jinja2==3.1.4
MarkupSafe==2.1.5
pytz==2024.1
six==1.16.0
SQLAlchemy==2.0.31
typing_extensions==4.12.2
Werkzeug==3.0.3
```

`.gitignore`

```text

# Ignore virtual environment
.venv/

# Ignore Python bytecode
__pycache__/

# Ignore environment variables
.env

# Ignore PyCharm project files
.idea/

# Ignore compiled Python files
*.pyc

# Ignore distribution/build files
dist/
build/

# Ignore generated HTML files
# *.html

# Ignore log files
*.log

# Ignore OS-specific files
.DS_Store
Thumbs.db
```

## (09:56) A Simple REST API

```py
# api.py

from flask import Flask


app = Flask(__name__)


@app.route('/')
def home():
    return '<h1>Flask Rest API</h1>'


if __name__ == '__main__':
    app.run(debug=True) # development ONLY !
```

## (12:38) Modeling Data & Creating the Database

```py
# api.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f'User(name = {self.name}, email = {self.email})'


@app.route('/')
def home():
    return '<h1>Flask Rest API</h1>'


if __name__ == '__main__':
    app.run(debug=True)
```

```py
# create_db.py
from api import app, db


with app.app_context():
    db.create_all()

```

##   (17:19) Flask Restful

```py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
api = Api(app)


class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f'User(name = {self.name}, email = {self.email})'


@app.route('/')
def home():
    return '<h1>Flask Rest API</h1>'


if __name__ == '__main__':
    app.run(debug=True)

```

##   (18:26) Define args with RequestParser

```py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
api = Api(app)


class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f'User(name = {self.name}, email = {self.email})'


user_args = reqparse.RequestParser()
user_args.add_argument('name', type=str, required=True,
                       hel='Name cannot be blank')
user_args.add_argument('email', type=str, required=True,
                       hel='Email cannot be blank')


@app.route('/')
def home():
    return '<h1>Flask Rest API</h1>'


if __name__ == '__main__':
    app.run(debug=True)

```

##   (19:51) /api/users Resource Endpoint

##   (21:54) Marshalling / Serializable JSON Data

##   (24:00) POST Data

##   (30:17) /api/users/id Resource Endpoint

##   (33:22) Update & Delete Data
