# Problem: Maximum Binary Tree - https://leetcode.com/problems/maximum-binary-tree/

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        if not nums: return
        rootVal = max(nums)
        idx = nums.index(rootVal)
        root = TreeNode(rootVal)
        root.left = self.constructMaximumBinaryTree(nums[:idx])
        root.right = self.constructMaximumBinaryTree(nums[idx+1:])
        return root