# Problem: Shuffle String - https://leetcode.com/problems/shuffle-string/description/

class Solution:
    def restoreString(self, s, indices):
        n = len(s)
        shuffled = [''] * n

        for i in range(n):
            shuffled[indices[i]] = s[i] 
        
        return ''.join(shuffled)  
