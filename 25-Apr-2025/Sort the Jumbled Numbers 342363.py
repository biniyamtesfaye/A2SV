# Problem: Sort the Jumbled Numbers - https://leetcode.com/problems/sort-the-jumbled-numbers/

class Solution(object):
    def sortJumbled(self, mapping, nums):
        def value(d):
            if d == 0: return mapping[0]
            res = 0
            curr = 1
            while d:
                d, r = divmod(d, 10)
                res += curr * mapping[r]
                curr *= 10
            return res
        nums.sort(key = value)
        return nums