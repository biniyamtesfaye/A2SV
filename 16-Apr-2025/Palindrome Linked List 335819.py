# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

class Solution: 

    def isPalindrome(self, head):
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        node = None
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt
        while node: 
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True