# Problem:  Longest Square Streak in an Array - https://leetcode.com/problems/longest-square-streak-in-an-array/description/?envType=problem-list-v2&envId=sorting

class Solution:
    def longestSquareStreak(self, nums):
        nums = sorted(set(nums))  
        num_set = set(nums)
        max_length = -1
        
        for num in nums:
            length = 1
            current = num
            
            while current * current in num_set:
                length += 1
                current = current * current 
            
            if length >= 2:
                max_length = max(max_length, length)
        
        return max_length
