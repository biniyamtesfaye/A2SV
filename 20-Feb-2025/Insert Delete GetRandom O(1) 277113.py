# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/description/

import random

class RandomizedSet(object):
    def __init__(self):
        self.list = []
        self.map = {}

    def insert(self, val):
        if val in self.map:
            return False
        
        self.list.append(val)
        self.map[val] = len(self.list) - 1
        return True

    def remove(self, val):
        if val not in self.map:
            return False
        
        index = self.map[val]
        last_element = self.list[-1]

        self.list[index] = last_element
        self.map[last_element] = index

        self.list.pop()
        del self.map[val]
        return True

    def getRandom(self):
        return random.choice(self.list)
