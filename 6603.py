


def dps(lotto_numbers, start_index, lst):
    if len(lst) == 6:
        print(*lst)
        return

    for i in range(start_index, len(lotto_numbers)):

        lst.append(lotto_numbers[i])
        dps(lotto_numbers, i + 1, lst)
        lst.pop()  # 백트래킹


first_run = True

while True:
    line = input().split()
    if not line:
        break

    lotto = list(map(int, line))

    if lotto[0] == 0:
        break

    if not first_run:
        print()
    first_run = False

    lotto_numbers = lotto[1:]

    dps(lotto_numbers, 0, [])