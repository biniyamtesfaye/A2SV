# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles):
        piles.sort()
        n = len(piles) // 3  #total rounds
        max_coins = 0
        
        for i in range(n, len(piles), 2):  #pick every second highest pile
            max_coins += piles[i]

        return max_coins
    