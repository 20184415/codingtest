str=input()
arr=str.split('-')
result=0
int_arr=[]
def chunk(v):
    parts = v.split('+')
    nums = [int(x) for x in parts]
    return sum(nums)

result+=chunk(arr[0])
for i in range(1, len(arr)):

  result-=chunk(arr[i])

print(result)

