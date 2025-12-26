n = int(input())
lst = list(map(int, input().split()))
result = int(input())

lst.sort()
left = 0
right = n - 1
cnt = 0

while left < right:
    s = lst[left] + lst[right]
    if s == result:
        cnt += 1
        left += 1
        right -= 1
    elif s > result:
        right -= 1
    else:
        left += 1

print(cnt)

