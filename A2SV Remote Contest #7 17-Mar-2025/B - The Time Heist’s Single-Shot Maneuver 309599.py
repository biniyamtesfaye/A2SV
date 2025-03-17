# Problem: B - The Time Heist’s Single-Shot Maneuver - https://codeforces.com/gym/596004/problem/B

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b1 = b[0]
    prev = -float('inf')
    possible = True
    for i in range(n):
        original = a[i]
        transformed = b1 - a[i]
        if original >= prev and transformed >= prev:
            chosen = min(original, transformed)
        elif original >= prev:
            chosen = original
        elif transformed >= prev:
            chosen = transformed
        else:
            possible = False
            break
        prev = chosen
    print("YES" if possible else "NO")