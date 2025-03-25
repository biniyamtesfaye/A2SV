# Problem: Binary Search Tree to Greater Sum Tree - https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

class Solution:
    def bstToGst(self, root):
        total = 0
        stack = []
        n = root
        
        while n or stack:
            if not n:
                n = stack.pop()
            else:
                while n.right:
                    stack.append(n)
                    n = n.right
            total += n.val
            n.val  = total
            n = n.left
        return root