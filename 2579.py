


N = int(input())


scores = []
for _ in range(N):
    scores.append(int(input()))


    if N == 1:
        print(scores[0])
    if N == 2:
        print(scores[0] + scores[1])
    DP = [0] * N
    DP[0] = scores[0]
    DP[1] = scores[0] + scores[1]

    DP[2] = max(scores[0] + scores[2], scores[1] + scores[2])

    for i in range(3, N):
        DP[i] = max(DP[i - 2] + scores[i], DP[i - 3] + scores[i - 1] + scores[i])

    print(DP[N - 1])
