from flask import jsonify, make_response, Blueprint, request
from app.shared_data import items

home_bp = Blueprint('home', __name__)

@home_bp.route('/', methods=['GET'])
def checkout_cart():
    """Endpoint to get all items list."""
    
    return make_response(jsonify(items), 200)