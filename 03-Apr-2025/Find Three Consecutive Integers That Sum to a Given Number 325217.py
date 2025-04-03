# Problem: Find Three Consecutive Integers That Sum to a Given Number - https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/

class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num % 3 == 0:
            num //= 3
            return [num - 1, num, num + 1]
        return []