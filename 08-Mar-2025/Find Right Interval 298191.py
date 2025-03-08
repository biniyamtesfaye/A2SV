# Problem: Find Right Interval - https://leetcode.com/problems/find-right-interval/

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        result = [-1] * n
        indexed_starts = []
        for i in range(n):
            indexed_starts.append([intervals[i][0], i])

        indexed_starts.sort()

        def binary_search(target):
            left, right = 0, n - 1
            while left <= right:
                mid = (left + right) // 2
                if indexed_starts[mid][0] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left
        for i in range(n):
            end = intervals[i][1]
            idx = binary_search(end)

            if idx < n:
                result[i] = indexed_starts[idx][1]
        return result