# Problem: Backspace String Compare - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        final_s = ""
        final_t = ""

        for char in s:
            if char == "#":
                if len(final_s) > 0:
                    new_string = ""
                    for i in range(len(final_s) - 1):
                        new_string += final_s[i]
                    final_s = new_string
            else:
                new_string = final_s
                new_string += char
                final_s = new_string
        for char in t:
            if char == "#":
                if len(final_t) > 0:
                    new_string = ""
                    for i in range(len(final_t) - 1):
                        new_string += final_t[i]
                    final_t = new_string
            else:
                new_string = final_t
                new_string += char
                final_t = new_string
        #compare
        return final_s == final_t