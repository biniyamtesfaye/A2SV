# Problem: Product of the Last K Numbers - https://leetcode.com/problems/product-of-the-last-k-numbers/description/

class ProductOfNumbers:
    def __init__(self):
        self.prefix = [1]  #start with 1 to avoid multiplication issues

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix = [1]  #reset prefix since multiplying by zero erases previous values
        else:
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.prefix):  #if we have a zero in the last k elements
            return 0
        return self.prefix[-1] // self.prefix[-(k+1)]
