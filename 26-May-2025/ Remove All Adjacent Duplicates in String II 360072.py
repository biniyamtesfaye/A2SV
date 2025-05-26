# Problem:  Remove All Adjacent Duplicates in String II - https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/description/

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        distinct = set(s)
        toRemove = list()
        for char in distinct:
            toRemove.append(char*k)
        
        while True:
            start = s
            for dup in toRemove:
                if dup in s:
                    s = s.replace(dup, "")
            if start == s:
                return s