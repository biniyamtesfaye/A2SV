# Problem: Linked List Cycle II - https://leetcode.com/problems/linked-list-cycle-ii/

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow, fast = slow.next, fast.next
                return slow
        return None