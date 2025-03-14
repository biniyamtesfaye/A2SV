# Problem: Count Pairs Whose Sum is Less than Target - https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/

class Solution:
    def countPairs(self, nums, target):
        nums.sort()  
        left, right = 0, len(nums) - 1
        count = 0
        
        while left < right:
            if nums[left] + nums[right] < target:
                count += (right - left) 
                left += 1 
            else:
                right -= 1  
        
        return count
