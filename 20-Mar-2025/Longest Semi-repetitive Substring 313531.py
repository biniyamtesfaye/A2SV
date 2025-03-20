# Problem: Longest Semi-repetitive Substring - https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/

class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        left = 0
        max_length = 0
        count = 0  # Count of adjacent pairs

        for right in range(1, len(s)):
            if s[right] == s[right - 1]:
                count += 1

            while count > 1:
                if s[left] == s[left + 1]:
                    count -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length if max_length > 0 else len(s)
