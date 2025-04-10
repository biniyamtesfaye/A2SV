# Problem: Longest Palindromic Substring - https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        maxLength=1
        maxString=s[0]
        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                if j-i+1 > maxLength and s[i:j+1] == s[i:j+1][::-1]:
                    maxLength = j-i+1
                    maxString = s[i:j+1]

        return maxString