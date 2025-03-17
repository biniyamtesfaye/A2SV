# Problem: D - The Snap of Fury - https://codeforces.com/gym/596004/problem/D

def count_survivors(n, L):
    killed = [0] * (n + 1)
    
    for i in range(n):
        left = max(0, i - L[i])
        right = i - 1
        killed[left] += 1
        killed[right + 1] -= 1
    
    survivors = 0
    current = 0
    for i in range(n):
        current += killed[i]
        if current == 0:
            survivors += 1
    
    return survivors

n = int(input())
L = list(map(int, input().split()))
print(count_survivors(n, L))