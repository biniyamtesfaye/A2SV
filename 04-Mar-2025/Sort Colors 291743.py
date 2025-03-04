# Problem: Sort Colors - https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums):
        count = [0] * 3

        for num in nums:
            count[num] += 1

        index = 0
        for i in range(3):  
            for _ in range(count[i]):  
                nums[index] = i  
                index += 1  

        