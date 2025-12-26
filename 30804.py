# 슬라이딩윈도우문제


n = int(input())
lst = list(map(int, input().split()))
left =0
count={}
answer=0
for r in range(n):
    fruit = lst[r]
    count[fruit] = count.get(fruit, 0) + 1

    while len(count)>2:
        l_fruit = lst[left]
        count[l_fruit] -= 1
        if count[l_fruit] == 0:
            del count[l_fruit]
        left += 1

    answer = max(answer,r-left+1)

print(answer)


