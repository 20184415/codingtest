#주식 하나를 산다.
#원하는 만큼 가지고 있는 주식을 판다.
#아무것도 안한다.

t= int(input())

for i in range(t):
    n = int(input())
    lst=list(map(int, input().split()))
    max_=0
    lst.reverse()
    value =lst[0]
    for i in range (1,n):
        if lst[i]>value:
            value=lst[i]
        elif lst[i]<value: # 산다
            max_+=value-lst[i]

    print(max_)


