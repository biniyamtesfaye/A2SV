# Problem: Frequency Tracker - https://leetcode.com/problems/frequency-tracker/description/

class FrequencyTracker(object):
    def __init__(self):
        self.freq_map = {} 
        self.count_map = {} 

    def add(self, number):
        old_freq = self.freq_map.get(number, 0)
        new_freq = old_freq + 1
        
        self.freq_map[number] = new_freq
        
        if old_freq in self.count_map:
            self.count_map[old_freq] -= 1
            if self.count_map[old_freq] == 0:
                del self.count_map[old_freq]  
        
        self.count_map[new_freq] = self.count_map.get(new_freq, 0) + 1

    def deleteOne(self, number):
        if number in self.freq_map:
            old_freq = self.freq_map[number]
            new_freq = old_freq - 1
            
            self.count_map[old_freq] -= 1
            if self.count_map[old_freq] == 0:
                del self.count_map[old_freq]
            
            if new_freq > 0:
                self.count_map[new_freq] = self.count_map.get(new_freq, 0) + 1
                self.freq_map[number] = new_freq
            else:
                del self.freq_map[number]

    def hasFrequency(self, frequency):
        return frequency in self.count_map
