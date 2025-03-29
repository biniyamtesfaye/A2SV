# Problem: Heaters - https://leetcode.com/problems/heaters/


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        result = 0
        position = 0
        heaters = [float('-inf')] + heaters + [float('inf')]
        for house in houses:
            while house >= heaters[position]:
                position += 1
            r = min(house - heaters[position - 1], heaters[position] - house)
            result = max(result, r)
        return result