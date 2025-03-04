# Problem: Find Target Indices After Sorting Indices - https://leetcode.com/problems/find-target-indices-after-sorting-array/description/

class Solution:
    def countingSort(self, nums):
        count = [0] * 101 
        for num in nums:
            count[num] += 1  

        sorted_nums = []
        for i in range(101):  
            sorted_nums.extend([i] * count[i])  

        return sorted_nums

    def targetIndices(self, nums, target):
        sorted_nums = self.countingSort(nums)  
        result = []
        for i in range(len(sorted_nums)):
            if sorted_nums[i] == target:
                result.append(i)
        return result
    