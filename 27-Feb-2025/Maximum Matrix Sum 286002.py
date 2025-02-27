# Problem: Maximum Matrix Sum - https://leetcode.com/problems/maximum-matrix-sum/description/?envType=problem-list-v2&envId=matrix

class Solution:
    def maxMatrixSum(self, matrix):
        total_sum = 0
        neg_count = 0
        min_abs_val = float('inf')
        
        for row in matrix:
            for num in row:
                total_sum += abs(num)
                if num < 0:
                    neg_count += 1
                min_abs_val = min(min_abs_val, abs(num))
        
        return total_sum if neg_count % 2 == 0 else total_sum - 2 * min_abs_val
