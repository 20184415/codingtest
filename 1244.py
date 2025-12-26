n = int(input())
lst = list(map(int, input().split()))
num_stu = int(input())

for _ in range(num_stu):
    gen, witch = map(int, input().split())
    if gen == 1: # 남학생은 곱이니
        for i in range(witch-1,len(lst),witch):
            if lst[i] ==1:
                lst[i] = 0
            else:
                lst[i] = 1
    elif gen==2:
        idx=witch-1
        lst[idx] = 1 - lst[idx]
        k=1
        while idx-k>=0 and idx+k<=len(lst)-1 and lst[idx-k]==lst[idx+k]:
            if lst[idx-k]==1:
                lst[idx-k]=0
                lst[idx+k]=0
            else:
                lst[idx-k]=1
                lst[idx+k]=1
            k+=1


for i in range(n):
    print(lst[i], end=' ')
    if (i + 1) % 20 == 0:
        print()
if n % 20 != 0:
    print()


