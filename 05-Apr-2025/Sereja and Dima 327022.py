# Problem: Sereja and Dima - https://codeforces.com/problemset/problem/381/A

n = int(input())
cards = list(map(int, input().split()))
left = 0
right = n - 1
sereja = 0
dima = 0
is_sereja_turn = True

while left <= right:
    if cards[left] > cards[right]:
        chosen = cards[left]
        left += 1
    else:
        chosen = cards[right]
        right -= 1
    if is_sereja_turn:
        sereja += chosen
    else:
        dima += chosen
    is_sereja_turn = not is_sereja_turn

print(sereja, dima)