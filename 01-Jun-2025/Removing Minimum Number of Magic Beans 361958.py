# Problem: Removing Minimum Number of Magic Beans - https://leetcode.com/problems/removing-minimum-number-of-magic-beans/

class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        mins = float("inf")
        tot = sum(beans)
        n = len(beans)
        for i in range(n):        
            re = tot - beans[i]*(n-i)
            mins = min(re,mins)
        return mins