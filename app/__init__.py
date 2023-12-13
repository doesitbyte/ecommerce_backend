"""
Module: app

This module is the entry point for the Flask application. It initializes the Flask
app object and registers different API resources using Flask-RESTful.
"""

from flask import Flask
from flask_restful import Api
from app.shared_data import Cart, initialize_datastore

datastore = initialize_datastore()

def create_app():

    app = Flask(__name__)
    api = Api(app)

    # Register blueprints
    register_resources(api)
    register_blueprints(app)

    return app

def register_resources(api: Api):

    from app.cart import CartResource
    from app.coupon import CouponResource
    from app.admin import AdminResource

    api.add_resource(CartResource, '/cart/add', '/cart/remove', '/cart/get')
    api.add_resource(CouponResource, '/coupon/get', '/coupon/post')
    api.add_resource(AdminResource, '/admin/get', '/admin/post')

def register_blueprints(app: Flask):

    from app.cart import checkout_bp

    app.register_blueprint(checkout_bp)