# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution(object):
    def maxProduct(self, words):
        n = len(words)
        word_masks = []
        lengths = []

        for word in words:
            mask = 0
            for char in word:
                mask |= (1 << (ord(char) - ord('a'))) 
            word_masks.append(mask)
            lengths.append(len(word))

        max_product = 0
        for i in range(n):
            for j in range(i + 1, n):
                if word_masks[i] & word_masks[j] == 0: 
                    max_product = max(max_product, lengths[i] * lengths[j])

        return max_product
            