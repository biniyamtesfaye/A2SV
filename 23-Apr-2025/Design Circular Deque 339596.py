# Problem: Design Circular Deque - https://leetcode.com/problems/design-circular-deque/

class MyCircularDeque:

    def __init__(self, k: int):
        self.size=k
        self.q=[0]*self.size
        self.front=-1
        self.rear=-1

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.front=self.rear=0
        else:
            self.front=(self.front-1)%self.size 
        self.q[self.front]=value
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.front=self.rear=0
        else:
            self.rear=(self.rear+1)%self.size 
        self.q[self.rear]=value
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        item=self.q[self.front]
        if self.front==self.rear: 
            self.front=self.rear=-1
        else:
            self.front=(self.front+1)%self.size
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        item=self.q[self.rear]
        if self.front==self.rear:
            self.front=self.rear=-1
        else:
            self.rear=(self.rear-1)%self.size 
        return True

    def getFront(self) -> int:
        if self.front==-1:
            return -1
        return self.q[self.front]

    def getRear(self) -> int:
        if self.rear==-1:
            return -1
        return self.q[self.rear]

    def isEmpty(self) -> bool:
        return self.front==self.rear==-1

    def isFull(self) -> bool:
        if (self.rear + 1) % self.size == self.front:
            return True
        return False