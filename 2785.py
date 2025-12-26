n = int(input())
chains = list(map(int, input().split()))

chains.sort()
rings = 0
chain = n
result = 0

for i in range(n):
    rings += chains[i]
    chain -= 1

    if rings >= chain:

        result = chain
        break

print(result)



