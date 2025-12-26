def rotate_90(arr):
    n =len(arr)
    m = len(arr[0])

    new_arr =[[0 ]* n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            new_arr[j][n-1-i] = arr[i][j]
    return new_arr


origin = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
result = rotate_90(origin)
print(result)
# 시계
# rotated = list(map(list, zip(*arr)))[::-1]
# 반시계
# rotated = list(map(list, zip(*arr[::-1])))