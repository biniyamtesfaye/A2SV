# Problem: Determine Whether Matrix Can Be Obtained By Rotation - https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

class Solution:
    def rotate(self, mat):
        n = len(mat)
        return [[mat[n - j - 1][i] for j in range(n)] for i in range(n)]

    def findRotation(self, mat, target):
        for _ in range(4):  # 0°, 90°, 180°, 270°
            if mat == target:
                return True
            mat = self.rotate(mat)  # Rotate 90 degrees
        return False
