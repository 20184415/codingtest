n,k = map(int,input().split())
lst = list(map(int,input().split()))

arr=[]
ans=0
for i in range(k):
    arr.append(lst[i])

ans =sum(arr)
max_ans = ans
for r in range(k,n):
    ans += lst[r]
    ans -= lst[r-k]
    if ans> max_ans:
        max_ans = ans


print(max_ans)
