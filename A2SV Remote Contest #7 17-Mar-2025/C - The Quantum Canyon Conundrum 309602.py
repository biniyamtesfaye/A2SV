# Problem: C - The Quantum Canyon Conundrum - https://codeforces.com/gym/596004/problem/C

def is_true_canyon(n, a):
    segments = []
    i = 0
    while i < n:
        current = a[i]
        l = i
        while i < n and a[i] == current:
            i += 1
        r = i - 1
        segments.append((l, r))
    
    valid_segments = []
    for l, r in segments:
        left_cond = (l == 0) or (a[l-1] > a[l])
        right_cond = (r == n-1) or (a[r] < a[r+1])
        if left_cond and right_cond:
            valid_segments.append((l, r))
    
    return len(valid_segments) == 1

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if is_true_canyon(n, a):
        print("YES")
    else:
        print("NO")