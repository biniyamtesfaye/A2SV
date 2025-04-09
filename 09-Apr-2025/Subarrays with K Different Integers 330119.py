# Problem: Subarrays with K Different Integers - https://leetcode.com/problems/subarrays-with-k-different-integers/

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        freq1 = [0] * 20001
        freq2 = [0] * 20001
        l1 = l2 = 0
        count = 0
        distinct1 = distinct2 = 0

        for r in range(len(nums)):
            x = nums[r]
            freq1[x] += 1
            if freq1[x] == 1:
                distinct1 += 1

            freq2[x] += 1
            if freq2[x] == 1:
                distinct2 += 1

            while distinct1 > k:
                y = nums[l1]
                freq1[y] -= 1
                if freq1[y] == 0:
                    distinct1 -= 1
                l1 += 1

            while distinct2 > k - 1:
                y = nums[l2]
                freq2[y] -= 1
                if freq2[y] == 0:
                    distinct2 -= 1
                l2 += 1

            count += l2 - l1

        return count
