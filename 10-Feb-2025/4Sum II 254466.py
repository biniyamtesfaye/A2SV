# Problem: 4Sum II - https://leetcode.com/problems/4sum-ii/

class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        sum_count = defaultdict(int)

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                sum_count[nums1[i] + nums2[j]] += 1

        result = 0

        for i in range(len(nums3)):
            for j in range(len(nums4)):
                targetSum = -(nums3[i] + nums4[j])
                if targetSum in sum_count:
                    result += sum_count[targetSum]
        return result