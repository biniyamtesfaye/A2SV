# Problem: Minimum Recolors to Get K Consecutive Black Blocks - https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        min_ops = k
        white_count = 0
        for i in range(k):
            if blocks[i] == 'W':
                white_count += 1
        
        min_ops = min(min_ops, white_count)

        for i in range(k, n):
            if blocks[i] == 'W':
                white_count += 1
            if blocks[i - k] == 'W':
                white_count -= 1
            
            min_ops = min(min_ops, white_count)
        
        return min_ops