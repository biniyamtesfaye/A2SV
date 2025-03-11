# Problem: Continuous Subarray Sum - https://leetcode.com/problems/continuous-subarray-sum/

class Solution:
    def checkSubarraySum(self, nums, k):
        prefix_sum = 0
        remainder_map = {0: -1}  

        for i, num in enumerate(nums):
            prefix_sum += num
            remainder = prefix_sum % k  

            if remainder in remainder_map:
                if i - remainder_map[remainder] > 1:
                    return True
            else:
                remainder_map[remainder] = i  

        return False
