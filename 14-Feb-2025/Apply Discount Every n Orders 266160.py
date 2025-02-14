# Problem: Apply Discount Every n Orders - https://leetcode.com/problems/apply-discount-every-n-orders/description/

from collections import defaultdict

class Cashier(object):
    def __init__(self, n, discount, products, prices):
        self.n = n  
        self.discount = discount  
        self.customer_count = 0  
        self.product_prices = {products[i]: prices[i] for i in range(len(products))}

    def getBill(self, product, amount):
        self.customer_count += 1  
        bill = sum(self.product_prices[product[i]] * amount[i] for i in range(len(product)))
        if self.customer_count % self.n == 0:
            bill *= (100 - self.discount) / 100.0  
        return bill
