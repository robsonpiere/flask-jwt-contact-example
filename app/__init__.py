import os
from flask_restful import Api
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate

basedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "contacts.db")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{basedir}"
app.config["SECRET_KEY"] = b'Q\xa5\xb6\x0c\xdc\xe9\xba\xf8e\xb6\xec{\x0e\x95r\x88C\x82:\xb0\xc0\xd1\xf0x'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
api = Api(app)
db = SQLAlchemy(app)
CORS(app)

migrate = Migrate(app, db)

from app.resources.contacts import Contatcs
api.add_resource(Contatcs, "/contacts")

from app.resources.auth import Login, Register
api.add_resource(Login, "/login")
api.add_resource(Register, "/register")
