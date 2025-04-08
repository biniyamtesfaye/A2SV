# Problem: Number of Substrings Containing All Three Characters - https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/

class Solution:  
    def numberOfSubstrings(self, s: str) -> int:
        result, lb, count = 0, -1, {c : 0 for c in 'abc'}
        for hb, c in enumerate(s):
            count[c] += 1
            while all(count.values()):
                result += len(s) - hb
                lb += 1
                count[s[lb]] -= 1
        return result