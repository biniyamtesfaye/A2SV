# Problem: Transformed Array - https://leetcode.com/problems/transformed-array/description/

class Solution:
  def constructTransformedArray(self, nums: List[int]) -> List[int]:
    n = len(nums)
    res = [0] * n
    for i in range(n):
      res[i] = nums[(i + nums[i]) % n]
    return res