# Problem: Zero Array Transformation III - https://leetcode.com/problems/zero-array-transformation-iii/description/

class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort(key=lambda x: x[0])
        query_idx = 0
        
        available = []
        events = [0] * (len(nums) + 1)
        prefix_sum = 0
        
        for i in range(len(nums)):
            prefix_sum += events[i]

            while query_idx < len(queries) and queries[query_idx][0] <= i:
                heappush(available, -queries[query_idx][1])
                query_idx += 1

            while prefix_sum < nums[i] and available and -available[0] >= i:
                prefix_sum += 1
                events[-heappop(available) + 1] -= 1
            if prefix_sum < nums[i]:
                return -1

        return len(available)