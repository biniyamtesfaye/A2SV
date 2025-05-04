# Problem: Maximum Sum With at Most K Elements - https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/description/

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:

        all_values = []

        for i in range(len(grid)):
            grid[i].sort(reverse=True)
            all_values.extend(grid[i][:limits[i]])

        all_values.sort(reverse=True)

        return sum(all_values[:k])