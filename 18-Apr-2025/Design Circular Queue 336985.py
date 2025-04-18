# Problem: Design Circular Queue - https://leetcode.com/problems/design-circular-queue/

class ListNode():
    def __init__(self,val=0, next=None):
        self.val = val
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.position = 0
        self.tail = self.head = None

    def enQueue(self, value: int) -> bool:
        if self.isFull(): 
            return False
        else:
            newNode = ListNode(value)
            if not self.head:
                self.head = self.tail = newNode
                self.head.next = self.head
            else:
                self.tail.next = newNode
                self.tail = newNode
                self.tail.next = self.head
            self.position += 1
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.tail.next = self.head
            self.position -= 1
            return True
        
    def Front(self) -> int:
        return -1 if self.isEmpty() else self.head.val

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.tail.val

    def isEmpty(self) -> bool:
        return self.position == 0

    def isFull(self) -> bool:
        return self.position == self.k