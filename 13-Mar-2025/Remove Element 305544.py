# Problem: Remove Element - https://leetcode.com/problems/remove-element/description/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        placeholder = 0

        for seeker in range(len(nums)):
            if nums[seeker] != val:
                nums[placeholder] = nums[seeker]
                placeholder += 1
        return placeholder