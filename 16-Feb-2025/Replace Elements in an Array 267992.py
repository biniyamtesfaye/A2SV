# Problem: Replace Elements in an Array - https://leetcode.com/problems/replace-elements-in-an-array/

class Solution(object):
    def arrayChange(self, nums, operations):
        index_map = {num: i for i, num in enumerate(nums)}
        
        for old, new in operations:
            idx = index_map.pop(old)  
            nums[idx] = new           
            index_map[new] = idx      
        
        return nums


            