

from collections import deque



def bfs(start_y, start_x, rain_height, visited):
    q = deque()
    q.append((start_y, start_x))
    visited[start_y][start_x] = 1

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]


            if 0 <= ny < n and 0 <= nx < n:

                if not visited[ny][nx] and arr[ny][nx] > rain_height:
                    visited[ny][nx] = 1
                    q.append((ny, nx))



n = int(input())
arr = []
max_h = 0

for i in range(n):
    lst = list(map(int, input().split()))
    arr.append(lst)
    max_h = max(max_h, max(lst))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

result = 0


for h in range(max_h):
    visited = [[0] * n for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(n):

            if arr[i][j] > h and visited[i][j] == 0:
                bfs(i, j, h, visited)
                cnt += 1

    if cnt > result:
        result = cnt

print(result)