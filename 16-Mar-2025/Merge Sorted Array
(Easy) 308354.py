# Problem: Merge Sorted Array
(Easy) - https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1, m, nums2, n):
        i, j, k = m - 1, n - 1, m + n - 1

        while j >= 0:  # Merge until nums2 is exhausted
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]  # Move the larger element
                i -= 1
            else:
                nums1[k] = nums2[j]  # Move nums2 element
                j -= 1
            k -= 1

        