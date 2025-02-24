# Problem: Fox And Snake - https://codeforces.com/problemset/problem/510/A

n, m = map(int, input().split())  

for row in range(1, n + 1):  
    if row % 2 == 1:  
        print("#" * m)  
    elif (row // 2) % 2 == 1:  
        print("." * (m - 1) + "#")  
    else:  
        print("#" + "." * (m - 1))  
