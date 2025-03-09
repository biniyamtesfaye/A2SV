# Problem: Smallest Value of the Rearranged Number - https://leetcode.com/problems/smallest-value-of-the-rearranged-number/description/

class Solution:
    def smallestNumber(self, num):
        if num == 0:
            return 0
        
        str_num = str(num)
        if num > 0:
            digits = sorted(str_num)
            if digits[0] == '0':
                for i in range(1, len(digits)):
                    if digits[i] != '0':
                        digits[0], digits[i] = digits[i], digits[0]
                        break
            return int("".join(digits))
        
        else:
            digits = sorted(str_num[1:], reverse=True)
            return int("-" + "".join(digits))
