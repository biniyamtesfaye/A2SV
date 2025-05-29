# Problem: Recover Binary Search Tree - https://leetcode.com/problems/recover-binary-search-tree/description/

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        a = b = prev = None
        stack = []

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if prev and root.val < prev.val:
                b = root
                if not a: a = prev
                else: break
            prev = root
            root = root.right
        a.val, b.val = b.val, a.val
        