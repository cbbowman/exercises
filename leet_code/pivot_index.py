def pivot_index(nums):
    index = 0
    length = len(nums)

    if length == 1:
        return index

    if length == 2:
        if nums[1] == 0:
            return index

        elif nums[0] == 0:
            index = 1

            return index

    for i, n in enumerate(nums):
        if i == 0:
            left_sum = 0
            right_sum = sum(nums[1:])
        else:
            left_sum += nums[i - 1]
            right_sum -= n

        if left_sum == right_sum:
            index = i

            return index
    index = -1

    return index


array = [3, 0]

pv = pivot_index(array)

print(pv)
