# Problem: A - How i met your mother - Last Forever - https://codeforces.com/gym/604857/problem/A

n = int(input())
s = input().strip()
count = {'z': 0, 'e': 0, 'r': 0, 'o': 0, 'n': 0}
for char in s:
    count[char] += 1

one = min(count['o'], count['n'], count['e'])
count['o'] -= one
count['n'] -= one
count['e'] -= one

# Calculate the number of 'zero's
zero = min(count['z'], count['e'], count['r'], count['o'])
count['z'] -= zero
count['e'] -= zero
count['r'] -= zero
count['o'] -= zero

result = ['1'] * one + ['0'] * zero
print(' '.join(result))