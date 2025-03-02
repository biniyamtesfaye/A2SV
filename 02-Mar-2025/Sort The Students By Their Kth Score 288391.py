# Problem: Sort The Students By Their Kth Score - https://leetcode.com/problems/sort-the-students-by-their-kth-score/

class Solution:
    def sortTheStudents(self, score, k):
        def sort_key(row):
            return row[k]

        score.sort(key=sort_key, reverse=True)
        return score

        