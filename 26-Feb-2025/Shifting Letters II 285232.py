# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s, shifts):
        n = len(s)
        diff = [0] * (n + 1)

        for start, end, direction in shifts:
            if direction == 1:
                diff[start] += 1
                diff[end + 1] -= 1
            else:
                diff[start] -= 1
                diff[end + 1] += 1

        shift = 0
        result = []
        
        for i in range(n):
            shift += diff[i] 
            new_char = chr(((ord(s[i]) - ord('a') + shift) % 26) + ord('a'))
            result.append(new_char)
        
        return "".join(result)

    