# Problem: Contains Duplicate - https://leetcode.com/problems/contains-duplicate/description/

class Solution(object):
    def containsDuplicate(self, nums):
        check = set()
        for num in nums:
            if num in check:
                return True
            check.add(num)
        return False
        