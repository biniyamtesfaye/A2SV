# Problem: Find the Kth Largest Integer in the Array - https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/

class Solution:
    def kthLargestNumber(self, nums, k):
        def custom_sort(x):
            return (len(x), x) 
        
        nums.sort(key=custom_sort)  
        return nums[-k]  
