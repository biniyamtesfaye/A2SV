# Problem: The k-th Lexicographical String of All Happy Strings of Length n - https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/description/

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        happy_set = {
            "a": "bc",
            "b": "ac",
            "c": "ab"
        }
        max_combinations = 3
        if n > 1:
            max_combinations *= 2**(n-1)

        if max_combinations < k:
            return ""

        result = ""
        last_char = ""
        while n > 0:
            if result:
                pointer = 0
                value = 2 ** (n - 1)
                if k > value:
                    pointer += 1
                    k -= value

                current_char = happy_set[last_char][pointer]
                result += current_char
                last_char = current_char
                n -= 1

            else:
                if k > (2 ** n):
                    result += "c"
                    last_char = 'c'
                    k -= (2 ** n)
                elif k > (2 ** (n - 1)):
                    result += "b"
                    last_char = 'b'
                    k -= (2 ** (n - 1))
                else:
                    result += "a"
                    last_char = 'a'

                n -= 1

        return result
        