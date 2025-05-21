# Problem: Minimum Cost to Hire K Workers - https://leetcode.com/problems/minimum-cost-to-hire-k-workers/description/

import heapq


class Solution:
    def mincostToHireWorkers(self, quality: list[int], wage: list[int], k: int) -> float:
        workers: list[tuple[float, int]] = sorted(
            (float(w) / q, q) for w, q in zip(wage, quality)
        )  # [(ratio, quality), ...]
        res: float = float("inf")
        quality_sum = 0
        heap: list[int] = (
            []
        )  

        for cur_ratio, q in workers:
            heapq.heappush(heap, -q)
            quality_sum += q
            if len(heap) > k:
                quality_sum += heapq.heappop(heap)
            if len(heap) == k:
                res = min(res, quality_sum * cur_ratio)

        return res