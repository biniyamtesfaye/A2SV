# Problem: Guess Number Higher or Lower  - https://leetcode.com/problems/guess-number-higher-or-lower/

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int, l=0) -> int:
        mid = (n+l)//2
        if guess(mid) == 0:
            return mid
        if guess(mid) == 1:
            return self.guessNumber(n, mid + 1)
        return self.guessNumber(mid - 1, l) 