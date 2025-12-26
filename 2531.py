n, d, k, c = map(int, input().split())
belt = [int(input()) for _ in range(n)]

count={}



for i in range(k):
    count[belt[i]] = count.get(belt[i], 0) + 1

max_kind = len(count) + (1 if c not in count else 0)

for i in range(n):
    out= belt[i]
    count[out] -=1
    if count[out] == 0:
        del count[out]

    in_=belt[(i+k)% n]
    count[in_] = count.get(in_, 0) + 1

    current = len(count) + (1 if c not in count else 0)
    max_kind = max(max_kind, current)


print(max_kind)