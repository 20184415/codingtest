n,m = map(int,input().split())
count={}

for i in range(n):
    word = input().strip()
    if len(word) >= m:
        count[word] = count.get(word, 0) + 1



sorted_words = sorted(count.keys(), key=lambda word: (-count[word], -len(word), word))

for word in sorted_words:
    print(word)