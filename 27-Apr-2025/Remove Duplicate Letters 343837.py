# Problem: Remove Duplicate Letters - https://leetcode.com/problems/remove-duplicate-letters/

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = [s[0]]
        count = Counter(s)
        for char in s[1:]:
            if char in stack:
                count[char] -= 1
                continue
            while stack and char<stack[-1] and count[stack[-1]] > 1:
                count[stack[-1]]-=1
                stack.pop()
            stack.append(char)
        return ''.join(stack)