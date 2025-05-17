# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution(object):
    def maxAbsoluteSum(self, nums):
        minSum=0
        maxSum=0
        prefixSum=0

        for i in range(0, len(nums)):
            prefixSum += nums[i]
            minSum=min(minSum, prefixSum)
            maxSum=max(maxSum, prefixSum)
        
        return maxSum-minSum