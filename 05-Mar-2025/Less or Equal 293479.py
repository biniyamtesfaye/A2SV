# Problem: Less or Equal - https://codeforces.com/problemset/problem/977/C

n, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

if k == 0:
    x = arr[0] - 1
    if 1 <= x <= 10**9:
        print(x)
    else:
        print(-1)
else:
    x = arr[k - 1]
    count = sum(1 for num in arr if num <= x)

    if count == k:
        print(x)
    else:
        print(-1)
