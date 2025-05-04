# Problem: K-th Symbol in Grammar - https://leetcode.com/problems/k-th-symbol-in-grammar/description/

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        
        prevLen = 1 << (n - 2)
        
        if k <= prevLen:
            return self.kthGrammar(n - 1, k)
        else:
            ans = self.kthGrammar(n - 1, k - prevLen)
            return 0 if ans == 1 else 1