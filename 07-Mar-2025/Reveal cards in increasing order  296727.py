# Problem: Reveal cards in increasing order  - https://leetcode.com/problems/reveal-cards-in-increasing-order/

from collections import deque
class Solution:
    def deckRevealedIncreasing(self, deck):
        deck.sort()  
        queue = deque()
        
        for card in reversed(deck):
            if queue:
                queue.appendleft(queue.pop())  
            queue.appendleft(card)
        
        return list(queue)
