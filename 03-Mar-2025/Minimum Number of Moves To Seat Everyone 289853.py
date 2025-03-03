# Problem: Minimum Number of Moves To Seat Everyone - https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/

class Solution:
    def minMovesToSeat(self, seats, students):
        seats.sort()
        students.sort()
        moves = 0
        for i in range(len(seats)):
            moves += abs(seats[i] - students[i])
        return moves

            