from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
start, end = map(int, input().split())
m = int(input())


graph = [[] for _ in range(n + 1)]


visited = [0] * (n + 1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(node,cnt):
    global result

    if node==end:
        result= cnt
        return
    visited[node] = True

    for n in graph[node]:
        if not visited[n]:
            dfs(n,cnt+1)


dfs(start, 0)
print(result)