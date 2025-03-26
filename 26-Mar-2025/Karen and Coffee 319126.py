# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

def preprocess(n, k, recipes):
    MAX_TEMP = 200000
    freq = [0] * (MAX_TEMP + 2)  

    for l, r in recipes:
        freq[l] += 1
        freq[r + 1] -= 1  

    recipe_count = [0] * (MAX_TEMP + 1)
    running_sum = 0

    for i in range(1, MAX_TEMP + 1):
        running_sum += freq[i]
        recipe_count[i] = running_sum  

    admissible = [0] * (MAX_TEMP + 1)

    for i in range(1, MAX_TEMP + 1):
        admissible[i] = 1 if recipe_count[i] >= k else 0  

    admissible_prefix = [0] * (MAX_TEMP + 1)
    
    for i in range(1, MAX_TEMP + 1):
        admissible_prefix[i] = admissible_prefix[i - 1] + admissible[i]  

    return admissible_prefix

def answer_queries(admissible_prefix, queries):
    for a, b in queries:
        print(admissible_prefix[b] - admissible_prefix[a - 1])

def main():
    n, k, q = map(int, input().split())
    
    recipes = [tuple(map(int, input().split())) for _ in range(n)]
    queries = [tuple(map(int, input().split())) for _ in range(q)]
    
    admissible_prefix = preprocess(n, k, recipes)
    answer_queries(admissible_prefix, queries)

if __name__ == "__main__":
    main()
