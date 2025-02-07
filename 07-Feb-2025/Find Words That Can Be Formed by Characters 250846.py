# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        chars_counter = Counter(chars)
        total_length = 0

        for word in words:
            word_counter = Counter(word)

            if all(word_counter[ch] <= chars_counter[ch] for ch in word):
                total_length += len(word)

        return total_length


        