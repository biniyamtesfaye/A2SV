# Problem: Remove Duplicate Letters - https://leetcode.com/problems/remove-duplicate-letters/

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        max_index = {}
        for i in range(len(s)):
            max_index[s[i]]  = i
        
        seen = set()
        stack = []
        for i in range(len(s)):
            if s[i] in seen:continue
            
            while stack and stack[-1]>s[i] and max_index[stack[-1]]>(i):
                seen.remove(stack[-1])
                stack.pop()
            stack.append(s[i])
            seen.add(s[i])
        return ''.join(stack)
        