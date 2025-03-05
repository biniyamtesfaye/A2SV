# Problem: Array Splitting - https://codeforces.com/problemset/problem/1197/C

n, k = map(int, input().split())
a = list(map(int, input().split()))

diffs = [a[i] - a[i - 1] for i in range(1, n)]
diffs.sort(reverse=True)

cost = sum(diffs[k - 1:])

print(cost)
