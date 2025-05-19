# Problem: Card Flipping Game - https://leetcode.com/problems/card-flipping-game/description/

class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        res = []
        bad = []
        for i, f in enumerate(fronts):
            if fronts[i] != backs[i]:
                res.append(fronts[i])
                res.append(backs[i])
            else:
                if fronts[i] in res:
                    res.remove(fronts[i])
                if backs[i] in res:
                    res.remove(backs[i])
                bad.append(fronts[i])
                bad.append(backs[i])
        print(res, bad)
        ans = float('inf')
        for r in res:
            if r not in bad:
                ans = min(ans, r)
        if ans == float('inf'):
            return 0
        return ans

        