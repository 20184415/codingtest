from collections import deque

c, b = map(int, input().split())
visited = [0] * 200001


def bfs(c, b):
    q = deque()
    q.append(b)
    visited[b] = 1
    time = 0

    while q:

        if c <= 200000 and visited[c] != 0:
            return time
        for _ in range(len(q)):
            cur = q.popleft()

            for i in (cur - 1, cur + 1, 2 * cur):
                if 0 <= i <= 200000 and visited[i] == 0:
                    q.append(i)
                    visited[i] = visited[cur] + 1

        time += 1
        c += time

        if c > 200000:
            return -1

    return -1


print(bfs(c, b))