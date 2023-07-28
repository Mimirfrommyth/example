import os
from flask import Flask, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

def create_app():
    app = Flask(__name__)
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://example_pqya_user:qLoewjGUu7slEM4eVXoFH8k436mKM1Ws@dpg-cj1v4295rnuhn3jaamm0-a.oregon-postgres.render.com/example_pqya'
    # postgres://example_pqya_user:qLoewjGUu7slEM4eVXoFH8k436mKM1Ws@dpg-cj1v4295rnuhn3jaamm0-a.oregon-postgres.render.com/example_pqya
    #db = SQLAlchemy(app)

        
    #Line below only required once, when creating DB.
    # with app.app_context():
    #     db.create_all()


    @app.route("/")
    def hello():
        return "Hello World!"



    return app