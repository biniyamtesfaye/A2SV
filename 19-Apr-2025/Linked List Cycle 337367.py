# Problem: Linked List Cycle - https://leetcode.com/problems/linked-list-cycle/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        while(slow):
            if slow.val == None:
                return True
            slow.val = None
            slow = slow.next
        return False