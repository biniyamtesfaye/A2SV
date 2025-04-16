# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        count = 0
        temp = self.head
        while temp:
            if count==index:
                return temp.data
            temp = temp.next
            count+=1
        return -1
            
    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        if index <= 0:
            self.addAtHead(val)
            return
        new_node = Node(val)
        count=0
        temp = self.head
        while temp:
            if count==index-1:
                new_node.next = temp.next
                temp.next = new_node
            temp=temp.next
            count+=1

    def deleteAtIndex(self, index: int) -> None:
        if index==0:
            if self.head:
                self.head = self.head.next
        temp = self.head
        count=0
        while temp:
            if count==index-1 and temp.next:
                temp.next = temp.next.next
            temp=temp.next
            count+=1


        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)