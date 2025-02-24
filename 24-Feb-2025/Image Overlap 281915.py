# Problem: Image Overlap - https://leetcode.com/problems/image-overlap/description/

from collections import Counter

class Solution:
    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        n = len(img1)  

        img1_ones = []
        img2_ones = []

        for r in range(n):
            for c in range(n):
                if img1[r][c] == 1:
                    img1_ones.append((r, c)) 
                if img2[r][c] == 1:
                    img2_ones.append((r, c)) 

        shift_counts = Counter()

        for (r1, c1) in img1_ones:  
            for (r2, c2) in img2_ones:  
                shift = (r2 - r1, c2 - c1) 
                shift_counts[shift] += 1

        return max(shift_counts.values(), default=0)
