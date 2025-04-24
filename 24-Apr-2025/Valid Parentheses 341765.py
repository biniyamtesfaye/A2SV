# Problem: Valid Parentheses - https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {')' : '(', '}': '{', ']': '['}

        for char in s:
            if char in brackets.values():
                stack.append(char)
            else:
                if not stack:
                    return False
                recent_opening_bracket = stack.pop()
                if recent_opening_bracket != brackets[char]:
                    return False
        return len(stack) == 0
                