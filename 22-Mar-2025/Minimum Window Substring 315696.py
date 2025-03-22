# Problem: Minimum Window Substring - https://leetcode.com/problems/minimum-window-substring/submissions/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_dict = {}
        for ch in t:
            t_dict[ch] = t_dict.get(ch, 0) + 1 
        window_dict = {}
        l, r = 0, 0
        res = [float(inf), ""]
        required = len(t_dict)
        count = 0
        while r < len(s):
            window_dict[s[r]] = window_dict.get(s[r], 0) + 1

            if s[r] in t_dict and window_dict[s[r]] == t_dict[s[r]]:
                count += 1
            r += 1
            while count == required:
                if r - l < res[0]:
                    res[0] = r-l
                    res[1] = s[l:r]
                window_dict[s[l]] -= 1
                if s[l] in t_dict and window_dict[s[l]] < t_dict.get(s[l], 0):
                    count -= 1
                l += 1
        return res[1]