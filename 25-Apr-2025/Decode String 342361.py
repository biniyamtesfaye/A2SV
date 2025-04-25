# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char != "]":
                stack.append(char)             
            else: 
                curr_str = ""
                while stack[-1] != "[":
                    curr_str = stack.pop() + curr_str
                stack.pop()
                current_num = ""

                while stack and stack[-1].isdigit():
                    current_num = stack.pop() + current_num
                curr_str = int(current_num) * curr_str
                stack.append(curr_str)

        return "".join(stack)
