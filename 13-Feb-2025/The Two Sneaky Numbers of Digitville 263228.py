# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution(object):
    def getSneakyNumbers(self, nums):
        seen = set()  #track seen numbers
        duplicates = []  #store duplicate numbers

        for num in nums:
            if num in seen:  #if number is already in the set its a duplicate
                duplicates.append(num)
            else:
                seen.add(num)  #else add to the set
        
        return duplicates  # Return the two duplicate numbers

            