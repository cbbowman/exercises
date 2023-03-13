def validMountainArray(arr):
    if len(arr) < 3:
        return False

    climbing = True

    if arr[1] - arr[0] <= 0:
        return False

    if arr[-2] - arr[-1] <= 0:
        return False

    for i, a in enumerate(arr):
        if i == 0:
            continue

        step = a - arr[i - 1]

        if step == 0:
            return False

        if climbing:
            if step < 0:
                climbing = False

            continue

        if step > 0:
            return False

    return not climbing


test_arr = [0, 3, 2, 1]

assert validMountainArray(test_arr) is True

test_arr2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

assert validMountainArray(test_arr2) is False
