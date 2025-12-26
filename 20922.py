n,k=map(int,input().split())
lst=list(map(int,input().split()))



left,right,ans = 0,0,0
cnt = [0] * (max(lst) + 1)
while right<n:
    if cnt[lst[right]]<k:
        cnt[lst[right]]+=1
        right+=1
    else:
        cnt[lst[left]]-=1
        left+=1
    ans=max(ans,right-left)
print(ans)