# Problem: Maximum Product of Three Numbers - https://leetcode.com/problems/maximum-product-of-three-numbers/description/

class Solution(object):
    def maximumProduct(self, nums):
        nums.sort()
        maxProduct1 = nums[-1] * nums[-2] * nums[-3]
        maxProduct2 = nums[0] * nums[1] * nums[-1] 
        if maxProduct1 > maxProduct2:
            maxProduct = maxProduct1
        else:
            maxProduct = maxProduct2

        return maxProduct