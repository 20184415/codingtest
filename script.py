#!/usr/bin/python3
import sys
sys.setrecursionlimit(10**6)

n, m, k = map(int, sys.stdin.readline().split())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
c = [[False]*m for _ in range(n)]
ans = -2147483647
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def go(cnt, s):
    global ans
    if cnt == k:
        if ans < s:
            ans = s
        return
    for x in range(n):
        for y in range(m):
            if c[x][y]:
                continue
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and c[nx][ny]:
                    break
            else:
                c[x][y] = True
                go(cnt + 1, s + a[x][y])
                c[x][y] = False

go(0, 0)
print(ans)
