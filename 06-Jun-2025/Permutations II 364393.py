# Problem: Permutations II - https://leetcode.com/problems/permutations-ii/description/

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=set()
        def per(nm: List[int],x: List[int]) -> None:
            if nm ==[]:
                aa=""
                for i in x:
                    aa+=str(i)+"*"
                res.add(aa)
            else:
                for i in range(len(nm)):    
                    nmc=nm[:i]+nm[i+1:]
                    xx=x.copy()
                    xx.append(nm[i])
                    per(nmc,xx)
        per(nums,[])
        r=[]
        for i in res:
            a=i.split('*')
            a.pop()
            b=[]
            for j in a:
                b.append(int(j))
            r.append(b)
        return r