N,K = map(int, input().split())
lst = list(map(int, input().split()))
M = int(input())
cnt =0
result =0
sum_ =0
def dfs(idx,cnt,sum_):
    global result
    if cnt == K:
        if sum_ % M == 0:
            result += 1
            return
    for i in range(idx, N):
        dfs(i + 1, cnt + 1, sum_ + lst[i])
dfs(0, cnt, sum_)
print(result)








