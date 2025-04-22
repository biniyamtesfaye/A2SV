# Problem: B - Friends - The Last One - https://codeforces.com/gym/604857/problem/B

t = int(input())
res = []
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = sum(a)
    mx = max(a)
    mn = min(a)
    if s + mx - mn + n <= m:
        res.append("YES")
    else:
        res.append("NO")
print("\n".join(res))
