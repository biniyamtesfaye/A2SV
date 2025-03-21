# Problem: Find the Punishment Number of an Integer - https://leetcode.com/problems/find-the-punishment-number-of-an-integer/description/

class Solution:
    def punishmentNumber(self, n):
        def can_partition(s, target, index=0, curr_sum=0):
            if index == len(s):  
                return curr_sum == target
            
            for j in range(index, len(s)):
                num = int(s[index:j+1])
                if curr_sum + num > target: 
                    break
                if can_partition(s, target, j+1, curr_sum + num):
                    return True
            return False
        
        total_punishment = 0
        
        for i in range(1, n + 1):
            square_str = str(i * i)
            if can_partition(square_str, i):
                total_punishment += i * i
        
        return total_punishment
