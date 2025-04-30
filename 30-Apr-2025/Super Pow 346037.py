# Problem: Super Pow - https://leetcode.com/problems/super-pow/description/

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        b = [str(i) for i in b]
        n = int("".join(b)) 
        def pow(x, n):
            if n == 0:
                return 1
            elif n%2==0:
                res =  pow(x, n>>1)%1337
                return res**2
            else:
                res = pow(x, (n-1)>>1)%1337
                return x*(res**2)
            
        return pow(a, n)%1337
        