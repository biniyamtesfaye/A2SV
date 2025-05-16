# Problem: Search in a BST - https://leetcode.com/problems/search-in-a-binary-search-tree/description/

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root:
            if root.val < val:
                return self.searchBST(root.right, val)
            elif root.val > val:
                return self.searchBST(root.left, val)
            else:
                return root