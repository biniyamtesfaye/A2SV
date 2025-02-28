# Problem: Remove Letter To Equalize Frequency - https://leetcode.com/problems/remove-letter-to-equalize-frequency/

from collections import Counter

class Solution:
    def equalFrequency(self, word: str) -> bool:
        freq = Counter(word)
        freq_count = Counter(freq.values())
        
        if len(freq_count) == 1:
            return len(freq) == 1 or 1 in freq_count
        
        if len(freq_count) == 2:
            freq_values = list(freq_count.keys())
            f1, f2 = min(freq_values), max(freq_values)
            
            if f1 == 1 and freq_count[f1] == 1:
                return True
            
            if f2 == f1 + 1 and freq_count[f2] == 1:
                return True
        
        return False
