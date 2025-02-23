# Problem: Chat Order - https://codeforces.com/problemset/problem/637/B

n = int(input())
friends = [input().strip() for _ in range(n)]

chatted = set()
result = []

for person in reversed(friends):
    if person not in chatted:
        result.append(person)
        chatted.add(person)

print("\n".join(result))
