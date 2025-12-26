from collections import deque


knight_moves = [
    (-2, -1), (-2, 1), #상
    (2, -1), (2, 1), # 하
    (-1, -2), (1, -2), # 좌
    (-1, 2), (1, 2) # 우
]


def bfs(W, st_y, st_x, end_y, end_x):
    if st_y == end_y and st_x == end_x:
        return 0

    visited = [[0] * W for _ in range(W)]

    q = deque([(st_y, st_x)])

    while q:
        y, x = q.popleft()

        for dy, dx in knight_moves:
            ny = y + dy
            nx = x + dx

            if 0 <= ny < W and 0 <= nx < W:

                if visited[ny][nx] == 0:

                    result = visited[y][x] + 1

                    if ny == end_y and nx == end_x:
                        return result

                    visited[ny][nx] = result
                    q.append((ny, nx))

    return -1


def solve():

    t = int(input())


    for _ in range(t):
            W = int(input())
            st_y, st_x = map(int, input().split())
            end_y, end_x = map(int, input().split())

            result = bfs(W, st_y, st_x, end_y, end_x)
            print(result)

solve()