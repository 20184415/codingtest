N,K,T = map(int,input().split())

shark = list(map(int,input().split()))

shark.sort()
stk=[] # 내가 먹을 수 있는 상어들 저장
# 1 5 10 15 24
idx = 0
for i in range(K):

    while idx < N and shark[idx]<T:
        stk.append(shark[idx])
        idx+=1
    if stk:
            T+=stk.pop()
    else:
            break




print(T)