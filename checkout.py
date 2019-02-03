__author__ = 'Vanessa'


class Checkout:

    total_price = 0  # Variable that will maintain the total value of the cart
    cart = {}  # Variable that will maintain the list of products and the quantity

    def __init__(self, rules):
        self.rules = rules

        # Initializing the cart with no items
        for item in rules:
            self.cart[item] = 0

    def scan(self, item):
        """
        In this function we'll check if the item exists in the list of products.
        If the product exists we will add in the cart,
        add the price to the total we already have of previous products
        and calculate the discount (if there is discount for the product)
        :param item: Product
        :return: None
        """
        item_detail = self.rules.get(item)
        if item_detail:
            self.cart[item] += 1
            self.total_price += item_detail.get('unit price')
            if item_detail.get('discount items'):
                self.calc_discount(item)

    def calc_discount(self, item_detail):
        """
        Function that calculates the discount on the product if it has reached the pre-established quantity
        :param item_detail: Details of the previously registered item
        :return: None
        """
        num_items = self.cart.get(item_detail)
        item_detail = self.rules.get(item_detail)
        discount_items = item_detail.get('discount items')

        if discount_items and (num_items == discount_items):
            discount = (discount_items * item_detail.get('unit price')) - item_detail.get('special price')
            self.total_price -= discount

    def total(self):
        return self.total_price
