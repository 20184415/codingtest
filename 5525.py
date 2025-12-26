n = int(input().strip())
m = int(input().strip())
s = input().strip()

answer = 0
cnt = 0
i = 1
while i < m - 1:
    if s[i-1:i+2] == 'IOI': # 중심을 "O"로 고정
        cnt += 1
        i += 2
        if cnt == n:
            answer += 1
            cnt -= 1
    else:
        cnt = 0
        i += 1
print(answer)

