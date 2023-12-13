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