# Problem: Count Good Numbers - https://leetcode.com/problems/count-good-numbers/

class Solution(object):
    def countGoodNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
        even=5
        prime=4
        mod=10**9+7
        if n%2==0:
            nevens=pow(even,n//2,mod)
            nprimes=pow(prime,n//2,mod)
        else:
            nevens=pow(even,(n//2)+1,mod)
            nprimes=pow(prime,n//2,mod)

        return (nevens*nprimes)%mod

        