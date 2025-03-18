# Problem: Maximum Average Subarray I  - https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, nums, k):
        n = len(nums)
        window_sum = sum(nums[:k])
        max_sum = window_sum
        for right in range(k, n):
            window_sum += nums[right] - nums[right - k]  
            max_sum = max(max_sum, window_sum) 

        return max_sum / k 
