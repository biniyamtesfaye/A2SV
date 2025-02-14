# Problem: Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution(object):
    def isCovered(self, ranges, left, right):
        covered_numbers = set()

        for start, end in ranges:
            for num in range(start, end + 1):
                covered_numbers.add(num)
        for num in range(left, right + 1):
            if num not in covered_numbers:
                return False
        return True

        
        