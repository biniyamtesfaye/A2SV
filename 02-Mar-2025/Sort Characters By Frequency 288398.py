# Problem: Sort Characters By Frequency - https://leetcode.com/problems/sort-characters-by-frequency/description/

class Solution:
    def frequencySort(self, s):
        freq = {}
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

        freq_list = []
        for key in freq:
            freq_list.append((key, freq[key]))

        for i in range(len(freq_list)):
            for j in range(i + 1, len(freq_list)):
                if freq_list[i][1] < freq_list[j][1]:
                    freq_list[i], freq_list[j] = freq_list[j], freq_list[i]

        result = []
        for char, count in freq_list:
            result.append(char * count)

        return "".join(result)
