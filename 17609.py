n=int(input())
def pal(l,r,s):

    while l<r:
        if s[l]==s[r]:
            l+=1
            r-=1
        else:
            return False
    return True

for _ in range(n):
    s = input().strip()
    l, r = 0, len(s) - 1

    while l < r :
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            break

    if l >= r:
        print(0)
    else:
        if pal(l+1, r, s) or pal(l, r-1, s):
            print(1)
        else:
            print(2)



