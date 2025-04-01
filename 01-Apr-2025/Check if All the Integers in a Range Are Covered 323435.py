# Problem: Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges = sorted(ranges)
        for s,e in ranges:
            if  s<=left<=e:
                if s<=right<=e:
                    return True
                else:
                    left=e+1
        return False