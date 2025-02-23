# Problem: Happy Number - https://leetcode.com/problems/happy-number/description/

class Solution:
    def isHappy(self, n: int) -> bool:
        if n < 0:
            return False
        
        visited = set()
        
        while n not in visited:
            visited.add(n)
            n = sum(int(digit) ** 2 for digit in str(n)) 
            
            if n == 1:
                return True
        
        return False
