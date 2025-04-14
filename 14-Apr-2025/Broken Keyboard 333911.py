# Problem: Broken Keyboard - https://codeforces.com/problemset/problem/1251/A

t = int(input())
for _ in range(t):
    s = input().strip()
    groups = []
    if s:
        current = s[0]
        count = 1
        for c in s[1:]:
            if c == current:
                count += 1
            else:
                groups.append((current, count))
                current = c
                count = 1
        groups.append((current, count))
    res = set()
    for char, cnt in groups:
        if cnt % 2 == 1:
            res.add(char)
    print(''.join(sorted(res)))