# Problem: K Radius Subarray Averages - https://leetcode.com/problems/k-radius-subarray-averages/description/

class Solution:
  def getAverages(self, nums: List[int], k: int) -> List[int]:
    result = [-1]*len(nums)

    left, curWindowSum, diameter = 0, 0, 2*k+1
    for right in range(len(nums)):
      curWindowSum += nums[right]
      if (right-left+1 >= diameter):
        result[left+k] = curWindowSum//diameter
        curWindowSum -= nums[left]
        left += 1
    return result