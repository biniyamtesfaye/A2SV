# Problem: A - Operation Infinity Assembly: The Endgame Merge - https://codeforces.com/gym/596004/problem/A

t = int(input())

for _ in range(t):
  n, m, k = map(int, input().split())
  a = sorted(input().strip())
  b = sorted(input().strip())

  i, j = 0, 0
  count_a, count_b = 0, 0
  c = []

  while i < n and j < m:
    if (count_a < k and (count_b == k or a[i] < b[j])):
      c.append(a[i])
      i += 1
      count_a += 1
      count_b = 0
    else:
      c.append(b[j])
      j += 1
      count_b += 1
      count_a = 0
  print("".join(c))