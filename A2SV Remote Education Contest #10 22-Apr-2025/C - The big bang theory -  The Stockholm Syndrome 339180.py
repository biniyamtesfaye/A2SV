# Problem: C - The big bang theory -  The Stockholm Syndrome - https://codeforces.com/gym/604857/problem/C

n = int(input())
a = list(map(int, input().split()))
a.sort()
mex = 1
for x in a:
    if x >= mex:
        mex += 1
print(mex)
