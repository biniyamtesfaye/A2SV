# Problem: Reverse Odd Levels of Binary Tree - https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/

class Solution:
    def reverseOddLevels(self, root):
        queue = [root]
        level = 0

        while queue:
            if level % 2 == 1:
                left, right = 0, len(queue) - 1
                while left < right:
                    queue[left].val, queue[right].val = queue[right].val, queue[left].val
                    left += 1
                    right -= 1

            next_level = []
            for node in queue:
                if node.left:
                    next_level.append(node.left)
                    next_level.append(node.right)

            queue = next_level
            level += 1

        return root
