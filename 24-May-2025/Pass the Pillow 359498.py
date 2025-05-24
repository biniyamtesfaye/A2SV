# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/description/

class Solution(object):
    def passThePillow(self, n, time):
        stand, flag = 1, 1
        while time:
            time -= 1
            if flag:
                stand += 1
                if stand == n:
                    flag = not flag
            else:
                stand -= 1
                if stand == 1:
                    flag = not flag
        return stand