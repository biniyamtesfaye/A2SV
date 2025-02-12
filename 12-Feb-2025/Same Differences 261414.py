# Problem: Same Differences - https://codeforces.com/problemset/problem/1520/D

import sys
from collections import defaultdict

def count_pairs(n, a):
    diff_count = defaultdict(int)
    pair_count = 0

    for i in range(n):
        diff = a[i] - i
        pair_count += diff_count[diff]  # Count pairs with the same (a[i] - i)
        diff_count[diff] += 1  # Store count of this difference

    return pair_count

# Read input
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1
results = []

for _ in range(t):
    n = int(data[index])
    a = list(map(int, data[index + 1: index + 1 + n]))
    index += n + 1
    results.append(str(count_pairs(n, a)))

# Print all results at once for efficiency
sys.stdout.write("\n".join(results) + "\n")
