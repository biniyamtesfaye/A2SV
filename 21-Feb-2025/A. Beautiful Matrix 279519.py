# Problem: A. Beautiful Matrix - https://codeforces.com/problemset/problem/263/A

matrix = []
for _ in range(5):
    row = list(map(int, input().split(" ")))
    matrix.append(row)
        
for r in range(5):
    for c in range(5):
        if matrix[r][c] == 1:
            one_r = r
            one_c = c

distance = abs(one_c - 2) + abs(one_r - 2)
print(distance)