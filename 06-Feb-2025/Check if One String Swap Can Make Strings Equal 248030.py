# Problem: Check if One String Swap Can Make Strings Equal - https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description/

class Solution(object):
    def areAlmostEqual(self, s1, s2):
        if s1 == s2:
            return True
        diff = [(c1, c2) for c1, c2 in zip(s1, s2) if c1 != c2]

        return len(diff) == 2 and diff[0] == diff[1][::-1]
        print(areAlmostEqual("Below", "Hello"))


        