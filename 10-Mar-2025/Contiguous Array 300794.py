# Problem: Contiguous Array - https://leetcode.com/problems/contiguous-array/

class Solution:
    def findMaxLength(self, nums):
        sum_index = {0: -1}  
        prefix_sum = 0
        max_length = 0

        for i, num in enumerate(nums):
            prefix_sum += 1 if num == 1 else -1 

            if prefix_sum in sum_index:
                max_length = max(max_length, i - sum_index[prefix_sum])
            else:
                sum_index[prefix_sum] = i  

        return max_length
