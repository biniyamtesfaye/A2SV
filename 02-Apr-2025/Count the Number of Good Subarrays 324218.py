# Problem: Count the Number of Good Subarrays - https://leetcode.com/problems/count-the-number-of-good-subarrays/description/

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        freq = Counter()
        result = j = total = 0 
        for x in nums: 
            total += freq[x]
            freq[x] += 1
            while total >= k: 
                freq[nums[j]] -= 1
                total -= freq[nums[j]]
                j += 1
            result += j 
        return result 