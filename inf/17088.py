n = int(input())
lst = list(map(int, input().split()))
sum_ = [0] * len(lst)

for i in range(n):
    a = lst[i]
    cnt = 0

    for j in range(len(lst)):

        if sum_[j] == 0:
            cnt += 1

        if cnt == a + 1:
            sum_[j] = i + 1
            break

print(sum_)