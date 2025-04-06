# Problem: Ugly Number II - https://leetcode.com/problems/ugly-number-ii/

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        result=[1]
        prod_2=prod_3=prod_5=0
        for i in range(1,n):
            a=result[prod_2]*2
            b=result[prod_3]*3
            c=result[prod_5]*5
            m=min(a,b,c)
            result.append(m)
            if m==a:
                prod_2+=1
            if m==b:
                prod_3+=1
            if m==c:
                prod_5+=1
        return result[-1]