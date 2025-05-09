# Problem: Integer to English Words - https://leetcode.com/problems/integer-to-english-words/

class Solution:
    def numberToWords(self, num: int) -> str:
        def number_to_words_helper(num):
            digit_string = ["Zero", "One", "Two",   "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
            teens_string = ["Ten", "Eleven",  "Twelve",  "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
            ty_string = ["", "", "Twenty",  "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
            res = ""
            if num > 99:
                res += digit_string[num // 100] + " Hundred "
            num %= 100
            if num < 20 and num > 9:
                res += teens_string[num - 10] + " "
            else:
                if num >= 20:
                    res += ty_string[num // 10] + " "
                num %= 10
                if num > 0:
                    res += digit_string[num] + " "
        

            return res

        if num == 0:
            return "Zero"
        big_string = ["Thousand", "Million", "Billion"]
        result = number_to_words_helper(num % 1000)
        num //= 1000
        for i in range(3):
            if num > 0 and num % 1000 > 0:
                result = number_to_words_helper(num % 1000) + big_string[i] + " " + result
            num //= 1000
        
        length = len(result)
        return result if length == 0 else result[: length - 1]