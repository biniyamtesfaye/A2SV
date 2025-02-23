# Problem: Find the Number of Distinct Colors Among the Balls - https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/description/

class Solution:
    def queryResults(self, limit: int, queries: list[list[int]]) -> list[int]:
        ball_color = {}
        color_count = {} 
        result = []

        for x, y in queries:
           
            if x in ball_color:
                old_color = ball_color[x]
                color_count[old_color] -= 1
                if color_count[old_color] == 0:
                    del color_count[old_color]

            ball_color[x] = y
            if y in color_count:
                color_count[y] += 1
            else:
                color_count[y] = 1

            result.append(len(color_count))

        return result
