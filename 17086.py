from collections import deque



dr = [-1, +1, 0, 0, -1, -1, +1, +1]
dc = [0, 0, -1, +1, -1, +1, -1, +1]

N, M = map(int, input().split())


visited = [[0] * M for _ in range(N)]
queue = deque()
result = 0

for r in range(N):
    row = list(map(int, input().split()))

    for c in range(M):
        value = row[c]

        if value == 1:
            queue.append((r, c))
            visited[r][c] = 1

while queue:
    r, c = queue.popleft()

    cur = visited[r][c] - 1

    if cur > result:
        result = cur

    for i in range(8):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0:
            visited[nr][nc] = visited[r][c] + 1
            queue.append((nr, nc))

print(result)