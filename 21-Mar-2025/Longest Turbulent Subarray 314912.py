# Problem: Longest Turbulent Subarray - https://leetcode.com/problems/longest-turbulent-subarray/

class Solution:
    def maxTurbulenceSize(self, A: List[int]):
        start = 0
        maxLen = 1
        opr = 0
        
        for end in range(1,len(A)):
            if A[end] > A[end-1]:
                if opr == -1 or opr == 0:
                    opr = 1
                    maxLen = max(maxLen, end - start +1)
                else:
                    start = end-1;
            elif A[end] < A[end - 1]:
                if opr == 1 or opr == 0:
                    opr = -1
                    maxLen = max(maxLen, end - start + 1)
                else:
                    start = end-1
            elif A[end] == A[end - 1]:
                opr = 0
                start = end
        
        return maxLen