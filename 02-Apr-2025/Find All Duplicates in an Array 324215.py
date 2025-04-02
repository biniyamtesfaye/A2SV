# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution(object):
    def findDuplicates(self, nums):
        result = []
    
        for num in nums:
            index = abs(num) - 1  
            if nums[index] < 0:  
                result.append(abs(num))
            else:
                nums[index] = -nums[index]  
        
        return result