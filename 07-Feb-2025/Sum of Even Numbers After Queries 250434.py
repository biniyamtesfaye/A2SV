# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        
        even_sum = sum(x for x in nums if x % 2 == 0)
        result = []

        for val, index in queries:
            old_value = nums[index]  
            new_value = old_value + val  

            # Remove old value from sum if it was even
            if old_value % 2 == 0:
                even_sum -= old_value

            # Update the nums array
            nums[index] = new_value

            # Add new value to sum if it is even
            if new_value % 2 == 0:
                even_sum += new_value

            # Store the current even sum in result
            result.append(even_sum)

        return result

        