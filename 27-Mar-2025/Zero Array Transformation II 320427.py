# Problem: Zero Array Transformation II - https://leetcode.com/problems/zero-array-transformation-ii/

class Solution:
    def check(self, nums, queries, k):
        pre = [0] * (len(nums) + 1)

        for i in range(k + 1):
            pre[queries[i][0]] += queries[i][2]
            if queries[i][1] + 1 < len(pre):
                pre[queries[i][1] + 1] -= queries[i][2]

        for i in range(1, len(pre)):
            pre[i] += pre[i - 1]

        for i in range(len(nums)):
            if pre[i] < nums[i]:
                return False

        return True

    def minZeroArray(self, nums, queries):
        a = sorted(nums)

        if a[-1] == 0:
            return 0

        low, high = 0, len(queries) - 1
        ans = float('inf')

        while low <= high:
            mid = low + (high - low) // 2

            if self.check(nums, queries, mid):
                ans = mid + 1
                high = mid - 1
            else:
                low = mid + 1

        return -1 if ans == float('inf') else ans