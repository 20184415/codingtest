count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
s, p = map(int, input().strip().split())
dna_str = input().strip()
a, c, g, t = map(int, input().strip().split())

def is_valid():
    return (count['A'] >= a and
            count['C'] >= c and
            count['G'] >= g and
            count['T'] >= t)


for i in range(p):
    count[dna_str[i]] += 1

answer = 0

if is_valid():
    answer += 1

for r in range(p, s):
    left = r - p

    out = dna_str[left]
    in_ = dna_str[r]

    count[out] -= 1
    count[in_] += 1

    if is_valid():
        answer += 1

print(answer)
