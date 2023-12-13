from flask_restful import Resource, reqparse
from flask import jsonify, make_response
from app import datastore
from app.shared_data import *

coupons: CouponManager = datastore["coupons"]
orders: OrderHistory = datastore["orders"]

class CouponResource(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('coupon_code', type=str, required=True, help='Coupon code is required')
        super(CouponResource, self).__init__()

    def get(self):
        """Endpoint to get all coupon codes."""
        return coupons.coupon_codes

    def post(self):
        """Endpoint to validate a coupon code."""
        args = self.reqparse.parse_args()

        coupon_code = args['coupon_code']

        couponsData = coupons.coupon_codes

        # Check if the coupon code is valid
        if validateCoupon(coupon_code):
            coupon = coupons.coupon_codes.get(coupon_code)
            return make_response(jsonify(coupon), 200)
        else:
            return make_response(jsonify({'error': 'Invalid coupon code'}), 400)
        
def validateCoupon(coupon_code):
    couponsData = coupons.coupon_codes
    if coupon_code not in couponsData:
        return False
    if not couponsData.get(coupon_code)["claimed"] and orders.isEligibleForCoupon():
        return True
    else:
        return False