# Problem: Limited Repainting - https://codeforces.com/contest/2070/problem/C

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()
    a = list(map(int, input().split()))
    
    # Check if there are no B's
    if 'B' not in s:
        print(0)
        continue
    
    # Collect all possible X candidates: a_i and 0
    candidates = set()
    candidates.add(0)
    for num in a:
        candidates.add(num)
    candidates = sorted(candidates)
    
    left = 0
    right = len(candidates) - 1
    answer = float('inf')
    
    while left <= right:
        mid = (left + right) // 2
        X = candidates[mid]
        
        allowed_regions = []
        current_start = 0
        in_allowed = False
        for i in range(n):
            if s[i] == 'R' and a[i] > X:
                if in_allowed:
                    allowed_regions.append((current_start, i - 1))
                    in_allowed = False
                current_start = i + 1
            else:
                if not in_allowed:
                    current_start = i
                    in_allowed = True
        if in_allowed:
            allowed_regions.append((current_start, n - 1))
        
        required = 0
        for (start, end) in allowed_regions:
            has_mandatory = False
            for j in range(start, end + 1):
                if s[j] == 'B' and a[j] > X:
                    has_mandatory = True
                    break
            if has_mandatory:
                required += 1
        
        if required <= k:
            answer = X
            right = mid - 1
        else:
            left = mid + 1
    
    print(answer)