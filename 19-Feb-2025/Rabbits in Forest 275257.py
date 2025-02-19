# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

from collections import Counter

class Solution(object):
    def numRabbits(self, answers):
        count = Counter(answers)
        total_rabbits = 0

        for x, freq in count.items():
            group_size = x + 1  # A group consists of (x + 1) rabbits
            num_groups = (freq + x) // (x + 1)  # Number of such groups needed
            total_rabbits += num_groups * group_size  # Total rabbits from this group

        return total_rabbits

        