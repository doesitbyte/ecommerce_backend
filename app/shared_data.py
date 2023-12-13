"""
Module: shared_data

This module defines shared data structures and managers used across different parts
of the e-commerce application. It encapsulates classes for managing the shopping cart,
coupon codes, and other shared data.

Classes:
- Cart: Manages the state of the shopping cart, providing methods to add and remove items.
- CouponManager: Manages a set of valid coupon codes, providing methods to add new codes.
- PurchaseHistory: Manages and store the history of all checkout out orders.
"""

import json

items = json.load(open("items.json"))

class Cart:
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items = {}

    def add_item(self, item_id, quantity):
        """Add items to the shopping cart."""
        if item_id in self.items:
            self.items[item_id] += quantity
        else:
            self.items[item_id] = quantity

    def remove_item(self, item_id, quantity):
        """Remove items from the shopping cart."""
        if item_id in self.items:
            self.items[item_id] = max(0, self.items[item_id] - quantity)

    def to_dict(self):
        """Get items from the shopping cart, prices and total."""
        cartObject = {}
        itemsData = {}
        cartTotal = 0
        for item_id in self.items.keys():
            itemPrice = items[str(item_id)]
            itemQuantity = self.items[item_id]
            itemsData[item_id] = {
                "quantity": itemQuantity,
                "priceEach": itemPrice,
                "priceTotal": itemPrice*itemQuantity,
            }
            cartTotal += itemPrice*itemQuantity

        cartObject = {
            "items": itemsData,
            "cartTotal": cartTotal
        }

        return cartObject
    
class CouponManager:
    def __init__(self):
        """Initialize an empty set to store coupon codes."""
        self.coupon_codes = {}

    def add_coupon(self, coupon_code, discount_percent):
        """Add a new coupon code."""
        self.coupon_codes[coupon_code] = {
            "discount": discount_percent,
            "claimed": False
        }

    def claim_coupon(self, coupon_code):
        """Claim a coupon code."""
        try:
            self.coupon_codes.get(coupon_code)["claimed"] = True
        except:
            pass

    def to_dict(self):
        return self.coupon_codes
    
def initialize_datastore():
    cart = Cart()

    return {
        "cart": cart
    }