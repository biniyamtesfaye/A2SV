# Problem: Find geometric sum of the series using recursion - https://www.geeksforgeeks.org/find-geometric-sum-of-the-series-using-recursion/

def sum(n):
    if n == 0:
        return 1
    return 1 / pow(3, n) + sum(n-1)