# Problem: Maximum Matching of Players With Trainers - https://leetcode.com/problems/maximum-matching-of-players-with-trainers/

class Solution:
    def matchPlayersAndTrainers(self, players, trainers):
        players.sort()
        trainers.sort()
        
        i, j, count = 0, 0, 0
        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]: 
                count += 1
                i += 1 
            j += 1  
        
        return count
