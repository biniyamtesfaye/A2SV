# Problem: Smallest Range Covering Elements from K Lists - https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        comb_list = []
        ROWS = len(nums)
        if ROWS == 1:
            return [nums[0][0],nums[0][0]]
        for i in range(ROWS):
            for j in range(len(nums[i])):
                comb_list.append([nums[i][j], i])
        comb_list.sort()
        sw = {comb_list[0][1]: 1}
        l = 0
        res_diff = float("inf")
        res_i = 0
        res_j = 0
        for r in range(1, len(comb_list)):
            sw[comb_list[r][1]] = sw.get(comb_list[r][1], 0) + 1
            while len(sw) == ROWS:
                b = comb_list[r][0]
                a = comb_list[l][0]
                curr_diff = b - a
                if curr_diff < res_diff or (curr_diff == res_diff and a < res_i):
                    res_i = a
                    res_j = b
                    res_diff = curr_diff
                # pop from dict
                if sw[comb_list[l][1]] < 2:
                    sw.pop(comb_list[l][1])
                else:
                    sw[comb_list[l][1]] -= 1
                l += 1
        return [res_i, res_j]