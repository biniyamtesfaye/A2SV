# Problem: Find Consecutive Integers from a Data Stream - https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.count = 0
        self.queue = []

    def consec(self, num: int) -> bool:
        self.queue.append(num)
        
        if num == self.value:
            self.count += 1
        
        if len(self.queue) > self.k:
            removed = self.queue.pop(0)
            if removed == self.value:
                self.count -= 1
        
        return len(self.queue) >= self.k and self.count == self.k
