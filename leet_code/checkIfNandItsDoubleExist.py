from typing import List


def checkIfExist(arr: List[int]) -> bool:
    len_arr = len(arr)

    if len_arr < 2:
        return False

    hash_table = []

    for a in arr:
        double = 2 * a

        if double in hash_table:
            return True

        if a % 2 == 0:
            half = a // 2

            if half in hash_table:
                return True

        hash_table.append(a)

    return False

arr = [10, 2, 5, 3]
assert checkIfExist(arr) is True

arr = [3, 1, 7, 11]
assert checkIfExist(arr) is False

arr = [7, 1, 14, 11]
assert checkIfExist(arr) is True
