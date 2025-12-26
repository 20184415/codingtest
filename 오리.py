

dic_duck = {"q": 0, "u": 1, "a": 2, "c": 3, "k": 4}

sound = input().strip()

counts = [0] * 5
result = 0

if len(sound) % 5 != 0:
    print(-1)
    exit()

for char in sound:


    if char == "q":
        if counts[4] > 0:
            counts[4] -= 1
        else:
            result += 1

        counts[0] += 1


    else:
        if char not in dic_duck:
            print(-1)
            exit()

        cur = dic_duck[char]


        if counts[cur - 1] == 0:
            print(-1)
            exit()

        counts[cur - 1] -= 1
        counts[cur] += 1

for i in range(4):
    if counts[i] > 0:
        print(-1)
        exit()

print(result)
