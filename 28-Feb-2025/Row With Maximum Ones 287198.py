# Problem: Row With Maximum Ones - https://leetcode.com/problems/row-with-maximum-ones/

class Solution:
    def rowAndMaximumOnes(self, mat):
        max_ones = -1 
        row_index = -1

        for i in range(len(mat)): 
            ones_count = mat[i].count(1) 
            
            if ones_count > max_ones:
                max_ones = ones_count
                row_index = i 
                
        return [row_index, max_ones] 

