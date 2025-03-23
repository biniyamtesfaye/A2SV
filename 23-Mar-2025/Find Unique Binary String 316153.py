# Problem: Find Unique Binary String - https://leetcode.com/problems/find-unique-binary-string/description/

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
       mx=int("1"*len(nums),2)
       for i in range(mx+1):
        res=format(int(i), '0'+str(len(nums))+'b')
        if res not in nums:
            return res
       return ""        