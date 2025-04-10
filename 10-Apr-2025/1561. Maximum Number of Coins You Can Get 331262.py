# Problem: 1561. Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/description/

class Solution:
    def maxCoins(self, piles):
        piles.sort()
        n = len(piles) // 3
        max_coins = 0
        
        for i in range(n, len(piles), 2):  
            max_coins += piles[i]

        return max_coins
    