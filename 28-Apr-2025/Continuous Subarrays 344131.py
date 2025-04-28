# Problem: Continuous Subarrays - https://leetcode.com/problems/continuous-subarrays/

class Solution:
    def continuousSubarrays(self, nums):
        n, total, left, dict1 = len(nums), 0, 0, defaultdict(int)

        for right in range(n):
            dict1[nums[right]] += 1

            while max(dict1.keys()) - min(dict1.keys()) > 2:
                dict1[nums[left]] -= 1

                if dict1[nums[left]] == 0:
                    del dict1[nums[left]]

                left += 1

            total += right-left+1

        return total




