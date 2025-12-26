#x번 카드와 y번 카드를 골라 그 두 장에 쓰여진 수를 더한 값을 계산한다. (x ≠ y)
#계산한 값을 x번 카드와 y번 카드 두 장 모두에 덮어 쓴다.
import heapq

n,m=map(int,input().split())
lst= list(map(int, input().split()))

heapq.heapify(lst)

for i in range(n):
    a =heapq.heappop(lst)
    b = heapq.heappop(lst)
    s=a+b
    heapq.heappush(lst,s)
    heapq.heappush(lst,s)

print(sum(lst))