# Problem: B. Ehab Is an Odd Person - https://codeforces.com/problemset/problem/1174/B

n = int(input())
a = list(map(int, input().split()))
has_even = False
has_odd = False
for num in a:
    if num % 2 == 0:
        has_even = True
    else:
        has_odd = True
if has_even and has_odd:
    a.sort()
print(' '.join(map(str, a)))