# Problem: Merge Sorted Array
(Easy) - https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Pointers for nums1 and nums2
        p1, p2 = m - 1, n - 1
        # Pointer for the end of the merged array
        p = m + n - 1
        #code by Binyam
        # Traverse both arrays from the end to the beginning
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # If there are any remaining elements in nums2, copy them over
        # No need to copy remaining elements of nums1 since they are already in place
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p -= 1
            p2 -= 1
