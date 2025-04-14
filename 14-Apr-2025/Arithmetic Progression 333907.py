# Problem: Arithmetic Progression - https://codeforces.com/problemset/problem/382/C

n = int(input())
a = list(map(int, input().split()))
if n == 1:
    print(-1)
else:
    a_sorted = sorted(a)
    if n == 2:
        res = set()
        x, y = a_sorted
        if x == y:
            res.add(x)
        else:
            mid = (x + y)
            if mid % 2 == 0:
                res.add(mid // 2)
            res.add(2 * x - y)
            res.add(2 * y - x)
        res_sorted = sorted(res)
        print(len(res_sorted))
        if res_sorted:
            print(' '.join(map(str, res_sorted)))
    else:
        a_sorted = sorted(a)
        diffs = [a_sorted[i+1] - a_sorted[i] for i in range(len(a_sorted)-1)]
        all_same = all(d == diffs[0] for d in diffs)
        if all_same:
            d = diffs[0]
            res = set()
            if d == 0:
                res.add(a_sorted[0])
            else:
                res.add(a_sorted[0] - d)
                res.add(a_sorted[-1] + d)
            valid_res = []
            for candidate in res:
                new_list = sorted(a + [candidate])
                valid = True
                current_d = new_list[1] - new_list[0]
                for i in range(1, len(new_list)):
                    if new_list[i] - new_list[i-1] != current_d:
                        valid = False
                        break
                if valid:
                    valid_res.append(candidate)
            valid_res = sorted(valid_res)
            print(len(valid_res))
            if valid_res:
                print(' '.join(map(str, valid_res)))
        else:
            res = set()
            min_diff = min(diffs)
            valid = True
            cnt_twice = 0
            for d in diffs:
                if d != min_diff and d != 2 * min_diff:
                    valid = False
                    break
                if d == 2 * min_diff:
                    cnt_twice += 1
            if valid and cnt_twice == 1:
                pos = -1
                for i in range(len(diffs)):
                    if diffs[i] == 2 * min_diff:
                        pos = i
                        break
                inserted = a_sorted[pos] + min_diff
                res.add(inserted)
            max_diff = max(diffs)
            possible_d = max_diff // 2
            if max_diff % 2 == 0:
                valid2 = True
                cnt_max = 0
                for d in diffs:
                    if d == max_diff:
                        cnt_max += 1
                    elif d != possible_d:
                        valid2 = False
                        break
                if valid2 and cnt_max == 1:
                    pos = -1
                    for i in range(len(diffs)):
                        if diffs[i] == max_diff:
                            pos = i
                            break
                    inserted = a_sorted[pos] + possible_d
                    res.add(inserted)
            valid_res = []
            for candidate in res:
                new_list = sorted(a + [candidate])
                valid = True
                current_d = new_list[1] - new_list[0]
                for i in range(1, len(new_list)):
                    if new_list[i] - new_list[i-1] != current_d:
                        valid = False
                        break
                if valid:
                    valid_res.append(candidate)
            valid_res = sorted(valid_res)
            print(len(valid_res))
            if valid_res:
                print(' '.join(map(str, valid_res)))