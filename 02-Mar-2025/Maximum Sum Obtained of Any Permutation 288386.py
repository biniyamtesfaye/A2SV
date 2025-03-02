# Problem: Maximum Sum Obtained of Any Permutation - https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/description/

from typing import List

MOD = 10**9 + 7

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        # Step 1: Compute the coverage array
        coverage = [0] * (n + 1)
        for start, end in requests:
            coverage[start] += 1
            if end + 1 < n:
                coverage[end + 1] -= 1
        
        # Step 2: Calculate actual coverage using prefix sums
        for i in range(1, n):
            coverage[i] += coverage[i - 1]
        
        # Only need the first n elements of coverage
        #Code by Binyam
        coverage = coverage[:n]
        
        # Step 3: Sort nums and coverage in descending order
        nums.sort(reverse=True)
        coverage.sort(reverse=True)
        
        # Step 4: Calculate the maximum sum
        max_sum = sum(nums[i] * coverage[i] for i in range(n)) % MOD
        
        return max_sum
