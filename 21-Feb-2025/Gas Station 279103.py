# Problem: Gas Station - https://leetcode.com/problems/gas-station/

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        total_gas = sum(gas)
        total_cost = sum(cost)
        
        
        if total_gas < total_cost:
            return -1  

        start_index = 0
        tank = 0
        
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            
            if tank < 0:
                start_index = i + 1
                tank = 0
        
        return start_index

            