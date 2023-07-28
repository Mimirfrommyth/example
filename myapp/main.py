import os
from flask import Flask, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://example_pqya_user:qLoewjGUu7slEM4eVXoFH8k436mKM1Ws@dpg-cj1v4295rnuhn3jaamm0-a.oregon-postgres.render.com/example_pqya'
# postgres://example_pqya_user:qLoewjGUu7slEM4eVXoFH8k436mKM1Ws@dpg-cj1v4295rnuhn3jaamm0-a.oregon-postgres.render.com/example_pqya
db = SQLAlchemy(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    
#Line below only required once, when creating DB.
# with app.app_context():
#     db.create_all()


@app.route("/")
def hello():
    return "Hello World!"




if __name__ == "__main__":
    app.run()