from flask_restful import Resource, reqparse
from flask import jsonify, make_response
from app import datastore
from app.shared_data import *

coupons: CouponManager = datastore["coupons"]
orders: OrderHistory = datastore["orders"]

class AdminResource(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('coupon_code', type=str, required=True, help='Coupon code is required')
        self.reqparse.add_argument('discount_percent', type=float, required=True, help='Coupon code is required')
        super(AdminResource, self).__init__()

    def get(self):
        """Endpoint to get admin details."""
        adminDetails = orders.to_dict()
        adminDetails["coupons"] = coupons.coupon_codes
        
        return make_response(adminDetails, 200)

    def post(self):
        """Endpoint to add a coupon code."""
        args = self.reqparse.parse_args()

        coupon_code = args['coupon_code']
        discount_percent = args['discount_percent']

        coupons.add_coupon(coupon_code, discount_percent)

        return make_response(jsonify({"message": "Coupon added"}), 200)