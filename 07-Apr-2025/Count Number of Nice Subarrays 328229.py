# Problem: Count Number of Nice Subarrays - https://leetcode.com/problems/count-number-of-nice-subarrays/

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        right ,left = 0,0
        ans = 0 
        odd_cnt = 0
        ans = 0
        current_sub_count = 0
        for right in range(len(nums)):
            
            if nums[right]%2 == 1:
                odd_cnt += 1
                current_sub_count = 0
                
            while odd_cnt == k:
                if nums[left]%2 == 1:
                    odd_cnt -= 1
                current_sub_count += 1
                left += 1
                
            ans += current_sub_count
            
        return ans  