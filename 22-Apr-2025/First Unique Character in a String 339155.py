# Problem: First Unique Character in a String - https://leetcode.com/problems/first-unique-character-in-a-string/description/?envType=problem-list-v2&envId=queue

class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            if s[i] not in s[i+1:] and s[i] not in s[:i] :
                return i
        return -1
