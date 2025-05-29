# Problem: Validate Binary Search Tree - https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        result=[]
        def traversal(root):
            if root.left:
                traversal(root.left)
            result.append(root.val)
            if root.right:
                traversal(root.right)
        traversal(root)
        for i in range(len(result)-1):
            if result[i]>=result[i+1]:
                return False
        
        print(result)
        return True