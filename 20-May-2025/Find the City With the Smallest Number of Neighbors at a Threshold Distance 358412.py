# Problem: Find the City With the Smallest Number of Neighbors at a Threshold Distance - https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        from collections import defaultdict
        adj = defaultdict(list)
        for v1, v2, dist  in edges:
            adj[v1].append((v2,dist))  
            adj[v2].append((v1,dist))
        def dijkstra(src):
            heap = [(0,src)]
            visit = set()
            while heap:
                dist, node = heapq.heappop(heap)
                if node in visit: continue
                visit.add(node)
                for nei,dist2 in adj[node]:
                    nei_dist = dist + dist2
                    if nei_dist <= distanceThreshold:
                        heapq.heappush(heap,(nei_dist,nei))
            return len(visit)-1
        res, min_count = -1, n 
        for node in range(n):
            count = dijkstra(node)
            if count <= min_count:
                res = node
                min_count = count
        return res