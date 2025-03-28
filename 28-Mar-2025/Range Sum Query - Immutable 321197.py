# Problem: Range Sum Query - Immutable - https://leetcode.com/problems/range-sum-query-immutable/

from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        # Initialize prefix sum array
        self.prefix_sum = [0] * (len(nums) + 1)
        for i in range(1, len(self.prefix_sum)):
            self.prefix_sum[i] = self.prefix_sum[i - 1] + nums[i - 1]

    def sumRange(self, left: int, right: int) -> int:
        #Code by Binyam
        # Calculate the sum using the prefix sum array
        return self.prefix_sum[right + 1] - self.prefix_sum[left]
