# Problem: Isomorphic Strings - https://leetcode.com/problems/isomorphic-strings/

class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False

        s_to_t = {}
        mapped_t = set()

        for char_s, char_t in zip(s, t):
            if char_s in s_to_t:
                if s_to_t[char_s] != char_t:
                    return False
            else:
                if char_t in mapped_t:
                    return False
                s_to_t[char_s] = char_t
                mapped_t.add(char_t)

        return True

            