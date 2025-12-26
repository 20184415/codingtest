n, m = map(int, input().split())

lst=[]
def re(start):
        if len(lst)==m:
            print(' '.join(map(str, lst)))
            return

        for i in range(start,n+1):
            lst.append(i)
            re(i+1)
            lst.pop()


re(1)