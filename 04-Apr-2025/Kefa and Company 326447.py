# Problem: Kefa and Company - https://codeforces.com/problemset/problem/580/B

n, d = map(int, input().split())
friends = []
for _ in range(n):
    mi, si = map(int, input().split())
    friends.append((mi, si))
friends.sort()

max_total = 0
current_sum = 0
left = 0

for right in range(n):
    current_sum += friends[right][1]
    while friends[right][0] - friends[left][0] >= d:
        current_sum -= friends[left][1]
        left += 1
    if current_sum > max_total:
        max_total = current_sum

print(max_total)