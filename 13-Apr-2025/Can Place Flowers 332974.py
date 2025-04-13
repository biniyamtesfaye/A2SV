# Problem: Can Place Flowers - https://leetcode.com/problems/can-place-flowers/

class Solution: 
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count, previous = 0, 0

        for current in flowerbed:
            if current == 1:
                if previous == 1: # violation!
                    count -= 1
                previous = 1
            else:
                if previous == 1: # can't plant
                    previous = 0 
                else:
                    count += 1
                    previous = 1 # the current plot gets taken
            
        return count >= n