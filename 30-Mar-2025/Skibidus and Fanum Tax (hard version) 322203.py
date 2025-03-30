# Problem: Skibidus and Fanum Tax (hard version) - http://codeforces.com/problemset/problem/2065/C2

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b.sort()
    possible = True
    if m == 0:
        possible = False
    else:
        prev = min(a[0], b[0] - a[0])
        for i in range(1, n):
            required = prev + a[i]
            left = 0
            right = m - 1
            idx = m  
            while left <= right:
                mid = (left + right) // 2
                if b[mid] >= required:
                    idx = mid
                    right = mid - 1
                else:
                    left = mid + 1
            candidate1 = a[i] if a[i] >= prev else float('inf')
            if idx < m:
                candidate2 = b[idx] - a[i]
            else:
                candidate2 = float('inf')
            minimal = min(candidate1, candidate2)
            if minimal == float('inf'):
                possible = False
                break
            prev = minimal
    print("YES" if possible else "NO")