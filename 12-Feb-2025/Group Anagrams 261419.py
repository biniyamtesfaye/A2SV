# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution(object):
    def groupAnagrams(self, strs):
        anagram_groups = defaultdict(list)

        for word in strs:
            sorted_word = "".join(sorted(word))  # Sort characters of the word
            anagram_groups[sorted_word].append(word)  # Group by sorted word

        return list(anagram_groups.values())  # Convert dictionary values to list

        