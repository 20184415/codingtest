from collections import deque

f,s,g,u,d = map(int,input().split())


if s>g and d==0:
    print("use the stairs")
    exit()



visited =[0]* (f+1)
def bfs(s,g):
    q =deque()
    q.append(s)
    visited[s]=1
    while q:
        c=q.popleft()
        if c == g:
            return visited[c] - 1

        for next in (c + u, c - d):
            if 1 <= next <= f:
                if visited[next] == 0:
                    visited[next] = visited[c] + 1
                    q.append(next)

    return "use the stairs"

print(bfs(s,g))

