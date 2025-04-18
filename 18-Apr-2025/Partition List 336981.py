# Problem: Partition List - https://leetcode.com/problems/partition-list/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        dummy = ListNode(0)
        front = dummy
        dummy2 = ListNode(0)
        back = dummy2
        while head != None :
            if head.val < x :
                front.next = head
                front = front.next
            else :
                back.next = head
                back = back.next
            
            head = head.next
        
        back.next = None
        front.next = dummy2.next
        return dummy.next