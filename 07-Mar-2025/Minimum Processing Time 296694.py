# Problem: Minimum Processing Time - https://leetcode.com/problems/minimum-processing-time/

class Solution:
    def minProcessingTime(self, processorTime, tasks):
        processorTime.sort()
        tasks.sort(reverse=True)
        
        max_time = 0

        for i in range(len(processorTime)):
            assigned_tasks = tasks[i * 4: i * 4 + 4]
            largest_task = max(assigned_tasks)
            processor_finish_time = processorTime[i] + largest_task
            max_time = max(max_time, processor_finish_time)

        return max_time
