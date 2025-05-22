# Problem: Collect Coins in a Tree - https://leetcode.com/problems/collect-coins-in-a-tree/

class Solution:
    def collectTheCoins(self, coins, edges):
        if not edges:
            return 0

        n, dict1 = len(coins), defaultdict(set)

        for i,j in edges:
            dict1[i].add(j)
            dict1[j].add(i)

        leaves = [i for i in dict1 if len(dict1[i]) == 1]

        for u in leaves:
            while len(dict1[u]) == 1 and coins[u] == 0:
                p = dict1[u].pop()
                del dict1[u]
                dict1[p].remove(u)
                u = p

        for _ in range(2):
            leaves = [i for i in dict1 if len(dict1[i]) == 1]
            for u in leaves:
                p = dict1[u].pop()
                del dict1[u]
                dict1[p].remove(u)
                if len(dict1) < 2:
                    return 0

        return 2*(len(dict1)-1)
