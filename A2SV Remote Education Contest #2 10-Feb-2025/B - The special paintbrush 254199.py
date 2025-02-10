# Problem: B - The special paintbrush - https://codeforces.com/gym/586622/problem/B

t = int(input())

for _ in range(t):
  n = int(input())
  s = input()

  firstBlack = -1
  lastBlack = -1

  for i in range(n):
    if s[i] == 'B':
      if firstBlack == -1:
        firstBlack = i
      lastBlack = i

  minLength = lastBlack -firstBlack + 1
  print(minLength)