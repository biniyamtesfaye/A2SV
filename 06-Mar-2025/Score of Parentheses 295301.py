# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for char in s:
            if char == '(':
                stack.append(0)
            else:
                current_score = 0
                
                while stack and stack[-1] != 0:
                    current_score += stack.pop()
                stack.pop()
                stack.append(1 if current_score == 0 else 2 * current_score)
        return sum(stack)