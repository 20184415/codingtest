def rotate(arr):
    return [list(row) for row in zip(*arr[::-1])]


def check(new_lock, N, M):

    start_point = M

    for i in range(start_point, start_point + N):
        for j in range(start_point, start_point + N):
            if new_lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    M = len(key)
    N = len(lock)

    extended_size = M*3

    max_start = extended_size - M

    current_key = key
    for _ in range(4):
        current_key = rotate(current_key)

        for r_start in range(max_start):
            for c_start in range(max_start):

                new_lock = [[0] * extended_size for _ in range(extended_size)]

                for i in range(N):
                    for j in range(N):
                        new_lock[i + M][j + M] = lock[i][j]

                is_valid = True
                for i in range(M):
                    for j in range(M):
                        r = r_start + i
                        c = c_start + j

                        if new_lock[r][c] == 1 and current_key[i][j] == 1:
                            is_valid = False
                            break

                        new_lock[r][c] += current_key[i][j]
                    if not is_valid:
                        break

                if not is_valid:
                    continue
                if check(new_lock, N, M):
                    return True

    return False

