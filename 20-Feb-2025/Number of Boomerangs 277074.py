# Problem: Number of Boomerangs - https://leetcode.com/problems/number-of-boomerangs/description/

from collections import defaultdict

class Solution(object):
    def numberOfBoomerangs(self, points):
        boomerangs = 0

        for i in points:
            distance_map = defaultdict(int)

            for j in points: 
                if i == j:
                    continue  

                distance = (i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2
                distance_map[distance] += 1

            for count in distance_map.values():
                if count > 1:
                    boomerangs += count * (count - 1)

        return boomerangs
            