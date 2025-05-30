# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        answer = 0
        lastBucket = 0  

        if goal == 0:
            for num in nums:
                if num == 0:
                    lastBucket += 1
                    answer += lastBucket
                else:
                    lastBucket = 0
            return answer
        left = 0
        total = 0
        
        for right in range(len(nums)):
            total += nums[right]
            if total == goal:
                lastBucket = 0
            while total == goal:
                answer += 1
                lastBucket += 1
                total -= nums[left]
                left += 1
            if lastBucket != 0 and nums[right] == 0:
                answer += lastBucket
        return answer