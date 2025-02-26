# Problem: Car Pooling - https://leetcode.com/problems/car-pooling/description/

class Solution:
    def carPooling(self, trips, capacity):
        changes = [0] * 1001  #store passenger changes at each location
        
        #record pickups and drop-offs
        for numPassengers, start, end in trips:
            changes[start] += numPassengers  #pickup passengers
            changes[end] -= numPassengers    #drop-off passengers
        
        #traverse locations to check capacity
        current_passengers = 0
        for passengers in changes:
            current_passengers += passengers  #update the number of passengers in the car
            if current_passengers > capacity:
                return False  # Capacity exceeded at some point
        
        return True  #never exceeded capacity
