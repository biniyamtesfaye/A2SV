# Problem: Construct Smallest Number From DI String - https://leetcode.com/problems/construct-smallest-number-from-di-string/description/

class Solution:
    def smallestNumber(self, pattern):
        stack = []
        result = ""
        num = 1

        for char in pattern + "I":  
            stack.append(str(num))
            num += 1

            if char == "I":
                while stack:
                    result += stack.pop()

        return result
