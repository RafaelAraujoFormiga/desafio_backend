from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy


def init_app(app: Flask):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    mongo = SQLAlchemy(app)
    app.db = mongo.db
    return app
