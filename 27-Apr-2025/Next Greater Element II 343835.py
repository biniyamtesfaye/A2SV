# Problem: Next Greater Element II - https://leetcode.com/problems/next-greater-element-ii/

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        result = [-1] * len(nums)
        for _ in range(2):
            for i in range(len(nums)):
                while stack and nums[stack[-1]] < nums[i]:
                    result[stack.pop()] = nums[i]
                stack.append(i)
        return result