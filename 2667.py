from collections import deque

n=int(input())
arr=[]


visited = [0] * (n + 1)
graph=[[]* n for _ in range(n+1)]

frist,end= map(int,input().split())

m=int(input())
depth=0

for i in range(m):
    c,z =map(int,input().split())
    graph[c].append(z)
    graph[z].append(c)

def bfs(start,end):
    q=deque()
    q.append(start)
    visited[start]=0
    while q:
       now= q.popleft()

       if now==end:
           return visited[now]
       for i in graph[now]:
           if visited[i]==0:
               visited[i]=visited[now]+1
               q.append(i)
    return -1


result = bfs(frist, end)
print(result)