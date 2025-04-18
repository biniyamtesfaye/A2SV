# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/

class Solution:
    def pairSum(self, head):
        slow = head
        fast = head
        maxVal = 0

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        nextNode, prev = None, None
        while slow:
            nextNode = slow.next
            slow.next = prev
            prev = slow
            slow = nextNode

        while prev:
            maxVal = max(maxVal, head.val + prev.val)
            prev = prev.next
            head = head.next

        return maxVal