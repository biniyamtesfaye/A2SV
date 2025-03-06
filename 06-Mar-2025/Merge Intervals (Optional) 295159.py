# Problem: Merge Intervals (Optional) - https://leetcode.com/problems/merge-intervals/

class Solution:
    #sort intervals by start time
    def sort_inter(self, interval):
        return interval[0]
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=self.sort_inter)

        merged = []
        #merge overlapping intervals
        for interval in intervals:
            #if merged list is empty or no overlap add new interval
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            #else merge overlapping intervals by updating the end time
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged

        