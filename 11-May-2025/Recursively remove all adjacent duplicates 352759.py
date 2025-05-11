# Problem: Recursively remove all adjacent duplicates - https://www.geeksforgeeks.org/recursively-remove-adjacent-duplicates-given-string/

def remove_util(s, n):
    k = 0
    i = 0
    while i < n:
        if i < n - 1 and s[i] == s[i + 1]:
            while i < n - 1 and s[i] == s[i + 1]:
                i += 1
        else:
            # If not a duplicate, store the character
            s[k] = s[i]
            k += 1
        i += 1

    s = s[:k]
    if k != n:
        s = remove_util(list(s), k)
    
    return s

def rremove(s):
    s = list(s)
    
    return ''.join(remove_util(s, len(s)))
    