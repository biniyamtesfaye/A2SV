# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution(object):
    def numberOfPairs(self, nums):
        count = {}
        pairs = 0
        leftovers = 0

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        for key in count:
            pairs += count[key] // 2  #number of pairs
            leftovers += count[key] % 2  #leftover numbers and 1 if odd

        return [pairs, leftovers]
        