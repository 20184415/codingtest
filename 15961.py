n, d, k, c = map(int,input().split())
sushi = [int(input()) for _ in range(n)]

cnt = [0] * (d + 1)
dis = 0

for i in range(k):
    x = sushi[i]
    if cnt[x] == 0:
        dis += 1
    cnt[x] += 1

answer = dis
if cnt[c] == 0:
    answer = dis + 1

for s in range(1, n):
    out = sushi[s-1]
    cnt[out] -= 1
    if cnt[out] == 0:
        dis -= 1

    in_idx = (s + k - 1) % n
    inn = sushi[in_idx]

    if cnt[inn] == 0:
        dis += 1
    cnt[inn] += 1

    if cnt[c] == 0:
        cur = dis + 1
    else:
        cur = dis

    if cur > answer:
        answer = cur

print(answer)
