# Problem: Print 1 to n without using loops - https://www.geeksforgeeks.org/print-1-to-n-without-using-loops/

class Solution:
    def printTillN(self, n):
        def recursive_print(current):
            if current > n:
                return
            if current == n:
                print(current, end='')
            else:
                print(current, end=' ')
            recursive_print(current + 1)
        
        recursive_print(1)