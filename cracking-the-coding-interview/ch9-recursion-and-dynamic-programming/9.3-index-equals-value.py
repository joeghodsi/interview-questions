'''
Problem: Given a sorted array, write an algorithm that finds an index i such that arr[i] == i. Note:
    values are not guaranteed to be distinct
Solution: Sounds like a classic binary search. Note: still linear time because I go left and right
    regardless. I think I could make it smarter by considering if arr[i] < i then we only care about
    the right subarray but that doesn't work when the values are not guaranteed to be distinct
    - linear time, linear space
'''
from random import randint


def find_index_that_equals_value(arr):
    def _find_index_that_equals_value(arr, low, high):
        mid = (high + low) / 2
        if low > high:
            return
        if arr[mid] == mid:
            return mid
        left_subarray_ans = _find_index_that_equals_value(arr, low, mid - 1)
        right_subarray_ans = _find_index_that_equals_value(arr, mid + 1, high)
        return left_subarray_ans or right_subarray_ans

    return _find_index_that_equals_value(arr, 0, len(arr) - 1)


arr_size = 10
arr = [randint(0, arr_size - 1) for _ in xrange(arr_size)]
print arr
print find_index_that_equals_value(arr)
