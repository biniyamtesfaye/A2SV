# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], K: int) -> int:
        res = 0
        preRem = defaultdict(int)    
        prefix = 0                  

        for num in nums:
            prefix += num
            prefix = prefix % K

            if prefix == 0:
                res += 1

            if prefix in preRem:
                res += preRem[prefix]

            preRem[prefix] += 1

        return res
        