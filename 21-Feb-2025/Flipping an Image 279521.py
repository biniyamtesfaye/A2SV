# Problem: Flipping an Image - https://leetcode.com/problems/flipping-an-image/description/

class Solution(object):
    def flipAndInvertImage(self, image):
        n=len(image)
        #loop through each row
        for row in image:
            left, right = 0, n - 1
            while left <= right:
                row[left], row[right] = 1 - row[right], 1 - row[left]
                left += 1
                right -= 1
        return image
        #reverse each row and flip
        