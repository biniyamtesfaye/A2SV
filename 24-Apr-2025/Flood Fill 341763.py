# Problem: Flood Fill - https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
            start_color = image[sr][sc]
            if start_color == color:
                return image

            queue = [(sr, sc)]
            rows = len(image)
            cols = len(image[0])

            while queue:
                i, j = queue.pop()
                clr = image[i][j]

                if clr == color or clr != start_color: continue
                image[i][j] = color
                
                if i < rows - 1:
                    queue.append((i + 1, j))
                if i > 0:
                    queue.append((i - 1, j))

                if j < cols - 1:
                    queue.append((i, j + 1))
                if j > 0:
                    queue.append((i, j - 1))

            return image