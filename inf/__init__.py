n = int(input())
lst = list(map(int, input().split()))

avg = round(sum(lst) / n)

min_diff = abs(lst[0] - avg)
result_idx = 0

for idx, score in enumerate(lst):
    diff = abs(score - avg)

    if diff < min_diff:
        min_diff = diff
        result_idx = idx

    elif diff == min_diff:
        if score > lst[result_idx]:
            result_idx = idx

print(avg, result_idx+1)