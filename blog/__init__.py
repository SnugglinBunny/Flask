from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
app.config["SECRET_KEY"] = "b8947dde6d9375914e8e81dfd2781a5b"
db = SQLAlchemy(app)

from blog import routes
