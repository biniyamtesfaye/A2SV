# Problem: C - Sura loves coding - https://codeforces.com/gym/586622/problem/C

n = int(input())
s = input().strip()
word = []

for i in range(n-1, -1, -1):
  letter = s[i]

  length = len(word)

  if length % 2 == 0:
    pos = length // 2
  
  else:
    pos = length // 2

  word.insert(pos, letter)
original = ''.join(word)
print(original)