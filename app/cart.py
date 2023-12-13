from flask_restful import Resource, reqparse
from flask import jsonify, make_response, Blueprint, request
from app import datastore
from app.shared_data import *
from app.coupon import validateCoupon

checkout_bp = Blueprint('checkout', __name__)

cart: Cart = datastore["cart"]
orders: OrderHistory = datastore["orders"]
coupons: CouponManager = datastore["coupons"]

class CartResource(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('item_id', type=int, required=True, help='Item ID is required')
        self.reqparse.add_argument('quantity', type=int, required=True, help='Quantity is required')
        super(CartResource, self).__init__()

    def post(self):
        """Endpoint to add items to the shopping cart."""
        args = self.reqparse.parse_args()

        item_id = args['item_id']
        quantity = args['quantity']

        # Add item to the cart
        cart.add_item(item_id, quantity)

        return make_response(jsonify({'message': 'Item added to cart'}), 200)
    
    def delete(self):
        """Endpoint to remove items from the shopping cart."""
        args = self.reqparse.parse_args()

        item_id = args['item_id']
        quantity = args['quantity']

        # Remove item from the cart
        cart.remove_item(item_id, quantity)

        return make_response(jsonify({'message': 'Item removed from cart'}), 200)
    
    def get(self):
        """Endpoint to get current shopping cart"""

        return make_response(jsonify(cart.to_dict()), 200)

@checkout_bp.route('/cart/checkout', methods=['POST'])
def checkout_cart():
    """Endpoint to checkout the shopping cart."""
    
    data = request.get_json()
    if 'coupon_code' in data:
        if validateCoupon(data["coupon_code"]):
            coupon = coupons.coupon_codes[data["coupon_code"]]
            orders.checkout_cart(cart.to_dict(), coupon)
            coupons.claim_coupon(data["coupon_code"])
            cart.checkout_cart()
            return make_response(jsonify({"message": "Checkout out successfully"}), 200)
        else:
            return make_response(jsonify({"message": "Checkout failed. Invalid coupon."}), 400)
    else:
        orders.checkout_cart(cart.to_dict(), None)
        cart.checkout_cart()
        return make_response(jsonify({"message": "Checkout out successfully"}), 200)