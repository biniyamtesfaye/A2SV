# Problem: Median of Two Sorted Arrays - https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def find_kth_element(self, k, nums1, nums2):
        if not nums1:
            return nums2[k]
        if not nums2:
            return nums1[k]

        mid1 = len(nums1) // 2 
        mid2 = len(nums2) // 2  

        if mid1 + mid2 < k:
            if nums1[mid1] > nums2[mid2]:
                return self.find_kth_element(k - mid2 - 1, nums1, nums2[mid2 + 1:])
            else:
                return self.find_kth_element(k - mid1 - 1, nums1[mid1 + 1:], nums2)
        else:
            if nums1[mid1] > nums2[mid2]:
                return self.find_kth_element(k, nums1[:mid1], nums2)
            else:
                return self.find_kth_element(k, nums1, nums2[:mid2])

    def findMedianSortedArrays(self, nums1, nums2):
        total_size = len(nums1) + len(nums2)

        if total_size % 2 == 1:
            return self.find_kth_element(total_size // 2, nums1, nums2)
        else:
            k1 = total_size // 2
            k2 = total_size // 2 - 1
            num1 = self.find_kth_element(k1, nums1, nums2)
            num2 = self.find_kth_element(k2, nums1, nums2)
            return (num1 + num2) / 2.0