from typing import List


def insert_at_i(array, n, x):
    len_arr = len(array)
    for i in range(len_arr, x, -1):
        array[i - 1] = array[i - 2]
    array[x] = n
    return array


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    k = 0
    for i in range(m + n):
        if n - k == n + m - i:
            insert_at_i(nums1, nums2[k], i)
            k += 1
        else:
            for j in range(k, n):
                if nums2[j] < nums1[i]:
                    insert_at_i(nums1, nums2[j], i)
                    k += 1
    return nums1


a1 = [1, 2, 4, 6, 0, 0, 0, 0]
a2 = [3, 5, 7, 9]
m = merge(a1, 4, a2, 4)
print(m)
