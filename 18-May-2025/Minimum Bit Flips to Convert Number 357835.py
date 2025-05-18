# Problem: Minimum Bit Flips to Convert Number - https://leetcode.com/problems/minimum-bit-flips-to-convert-number/

class Solution(object):
    def minBitFlips(self, start, goal):
        result = start ^ goal
        count = 0
        while result:
            result &= result - 1
            count += 1
        return count