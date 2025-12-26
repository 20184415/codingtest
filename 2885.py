k=int(input())
i=0
value = 1
while value<k:

    value *=2
    i += 1

cho=value
cuts = 0
while k>0:
    if k>= value:
        k-=value
    else:
        value //=2
        cuts+=1

print(cho,cuts)