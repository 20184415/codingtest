s= input()

min_len= len(s)

for i in range(1,len(s)//2+1):
    cur =s[0:i]
    cnt=1
    compressed_string = ""
    for j in range(i,len(s),i):

        if cur == s[j:j+i]:
            cnt+=1
        else:
            if cnt > 1:
                compressed_string += str(cnt)
                compressed_string += cur
            else:
                compressed_string += cur
            cur = s[j:j + i]
            cnt=1
    if cnt>1:
        compressed_string += str(cnt)
        compressed_string += cur
    else:
        compressed_string += cur
    min_len=min(min_len,len(compressed_string))

print(min_len)