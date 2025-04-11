# Problem: Find All Anagrams in a String - https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

class Solution:
    def findAnagrams(self, string: str, anagram: str) -> List[int]:
        anagram = ''.join(sorted(anagram))
        window_string = ''       
        start_indices = []    
        window_start = 0
        
        for char in string:
            window_string += char
            if len(window_string) == len(anagram):
                if ''.join(sorted(window_string)) == anagram:
                    start_indices.append(window_start)
                window_string = window_string[1:]
                window_start += 1

        return start_indices
    