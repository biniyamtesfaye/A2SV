# Problem: Count the Number of Consistent Strings - https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution(object):
    def countConsistentStrings(self, allowed, words):
        allowedSet = set(allowed)
        count = 0

        for word in words:
            if all(char in allowedSet for char in word):
                count += 1
        return count