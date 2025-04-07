# Problem: Left-and-right-sum-differences - https://leetcode.com/problems/left-and-right-sum-differences/

from typing import List

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0] * n
        
        # Compute the total sum of the array
        total_sum = sum(nums)
        left_sum = 0
        
        # Calculate the left and right sums and their differences
        for i in range(n):
            #Code by Binyam
            # Right sum is total sum minus the sum of elements up to and including index i
            right_sum = total_sum - left_sum - nums[i]
            # Calculate the absolute difference
            answer[i] = abs(left_sum - right_sum)
            # Update the left sum for the next iteration
            left_sum += nums[i]
        
        return answer
