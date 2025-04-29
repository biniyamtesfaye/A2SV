# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        dp = {}
        
        def helper(l, r, p1):
            if l > r:
                return 0
            if (l, r, p1) in dp:
                return dp[(l, r, p1)]
            res = 0 if p1 else math.inf
            if p1:
                res = max(res, nums[l] + helper(l + 1, r, not p1), nums[r] + helper(l, r - 1, not p1))
            else:
                res = min(res, helper(l + 1, r, not p1), helper(l, r - 1, not p1))
            
            dp[(l, r, p1)] = res
            
            return res
        
        return helper(0, len(nums) - 1, True) >= sum(nums) / 2