# Problem: Largest Merge of Two Strings - https://leetcode.com/problems/largest-merge-of-two-strings/

class Solution:
    def largestMerge(self, w1: str, w2: str) -> str:
        answer=[]
        m, n = len(w1), len(w2)
        i=j=0
        while i < m or j < n:
            if w1[i:]>w2[j:]:
                answer.append(w1[i])
                i += 1
            else:
                answer.append(w2[j])
                j += 1
        return ''.join(answer)