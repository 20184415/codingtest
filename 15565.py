import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst = list(map(int, input().split()))

INF = 10**9
ans = INF
l = 0
cnt = 0

for r in range(n):
  if lst[r]==1:
    cnt += 1

  while cnt>=k:
      ans=min(ans,r-l+1)
      if lst[l]==1:
          cnt -= 1
      l += 1
print(ans)