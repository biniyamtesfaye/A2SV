# Problem: Power of Four - https://leetcode.com/problems/power-of-four/

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n > 0 and (n & (n - 1)) == 0:
            return n & 0x55555555 == n
        else:
            return False