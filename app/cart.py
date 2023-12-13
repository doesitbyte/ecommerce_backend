from flask_restful import Resource, reqparse
from flask import jsonify
from app.shared_data import Cart

cart = Cart()

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

        return jsonify({'message': 'Item added to cart'})
    
    def delete(self):
        """Endpoint to remove items from the shopping cart."""
        args = self.reqparse.parse_args()

        item_id = args['item_id']
        quantity = args['quantity']

        # Remove item from the cart
        cart.remove_item(item_id, quantity)

        return jsonify({'message': 'Item removed from cart'})
    
    def get(self):
        """Endpoint to get current shopping cart"""

        return jsonify(cart.to_dict())