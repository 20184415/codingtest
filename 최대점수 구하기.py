
n,m = map(int,input().split())
a = []
for _ in range(n):
    p,t = map(int,input().split())
    a.append((p,t))

res = 0

def dfs(st,sum_soc,sum_time):
    global  res
    if sum_soc > res:
        res = sum_soc

    for i in range(st,n):
        score = a[i][0]
        time = a[i][1]
        if sum_time+ time<= m:
            dfs(i+1,sum_soc+score,time+sum_time)
dfs(0,0,0)
print(res)







