# Problem: First Bad Version - https://leetcode.com/problems/first-bad-version/

class Solution:
    def firstBadVersion(self, n: int) -> int:
        return self.binarySearch(1, n)

    def binarySearch(self, left: int, right: int) -> int:
        if left == right: return left
        mid = (left + right) // 2
        if isBadVersion(mid):
            return self.binarySearch(left, mid)
        else:
            return self.binarySearch(mid + 1, right)