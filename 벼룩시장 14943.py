n =int(input())
lst = list(map(int, input().split()))
answer = 0
current_fleas = 0

for s in lst:
    current_fleas += s
    answer += abs(current_fleas)

print(answer)



