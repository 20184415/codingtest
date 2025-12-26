from collections import deque

n, k = map(int, input().split())
MAX = 100000
q = deque([(n, 0)])
visited = {n}

while True:
    x, t = q.popleft()
    if x == k:
        print(t)
        break
    for i in (x - 1, x + 1, x * 2):
        if 0 <= i <= MAX and i not in visited:
            visited.add(i)
            q.append((i, t + 1))
